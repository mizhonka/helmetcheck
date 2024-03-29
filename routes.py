from app import app
from flask import render_template, request, redirect
import re
import urllib.request
from search import Search
import pieces
import links

extras={ord("["):"", ord("]"):"", ord("'"):""}
all_libraries=[]
libraries=[]

def get_all_libraries():
    with open("all_libraries.txt", encoding="utf-8") as f:
        for lib in f:
            lib=lib.strip()
            if(lib):
                all_libraries.append(lib)

@app.route("/")
def index():
    if not all_libraries:
        get_all_libraries()
    return render_template("index.html", libraries=libraries, all_libraries=all_libraries)

@app.route("/add_library", methods=["POST"])
def add_library():
    library=request.form["lib_select"]
    if library not in libraries:
        libraries.append(library)
    return redirect("/")

@app.route("/delete_library/<string:library>")
def delete_library(library):
    libraries.remove(library)
    return redirect("/")

@app.route("/search", methods=["POST"])
def search():
    if not libraries:
        return redirect("/")
    search_links=links.get_included_links()
    result=Search(search_links, libraries).check_availability()
    return render_template("results.html", results=result, completeSearch=1)

@app.route("/search_piece/<int:id>")
def search_piece(id):
    if not all_libraries:
        get_all_libraries()
    piece_links=links.get_links(id)
    result=Search(piece_links, all_libraries).check_libraries()
    return render_template("results.html", results=result, completeSearch=0)

@app.route("/pieces")
def show_pieces():
    all_pieces=pieces.get_all()
    return render_template("pieces.html", pieces=all_pieces)

@app.route("/new_piece", methods=["POST"])
def new_piece():
    piece_name=request.form["name"]
    pieces.add_new(piece_name)
    return redirect("/pieces")

@app.route("/hide_piece/<int:id>")
def hide_piece(id):
    pieces.hide(id)
    return redirect("/pieces")

@app.route("/delete_piece/<int:id>")
def delete_piece(id):
    pieces.delete(id)
    return redirect("/pieces")

@app.route("/edit_piece/<int:id>/<int:invalid>/<int:new_name>")
def edit_piece(id, invalid, new_name):
    piece=pieces.get_by_id(id)
    piece_links=links.get_links(id)
    return render_template("piece_edit.html", piece=piece, piece_links=piece_links, invalid_link=invalid, new_name=new_name)

def validate_link(link,id):
    if links.link_exists(id, link):
        return False
    if not re.search("^https://haku.helmet.fi/iii/encore/record/", link):
        return False
    try:
        address=urllib.request.urlopen(link)
        address.read()
    except Exception:
        return False
    return True

@app.route("/add_link", methods=["POST"])
def add_link():
    id=request.form["id"]
    link=request.form["link"].strip()
    if not validate_link(link,id):
        return redirect(f"/edit_piece/{id}/{1}/{0}")
    links.add(id, link)
    return redirect(f"/edit_piece/{id}/{0}/{0}")

@app.route("/delete_link/<int:piece_id>/<int:id>")
def delete_link(piece_id,id):
    links.delete(id)
    return redirect(f"/edit_piece/{piece_id}/{0}/{0}")

@app.route("/edit_name/<int:id>")
def edit_name(id):
    return redirect(f"/edit_piece/{id}/{0}/{1}")

@app.route("/update_name", methods=["POST"])
def update_name():
    id=request.form["id"]
    new_name=request.form["new_name"].strip()
    if not new_name:
        return redirect(f"/edit_piece/{id}/{0}/{1}")
    pieces.update(id, new_name)
    return redirect(f"/edit_piece/{id}/{0}/{0}")
