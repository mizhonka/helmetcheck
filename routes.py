from app import app
from flask import render_template, request, redirect
from search import Search
import pieces
import links

extras={ord("["):"", ord("]"):"", ord("'"):""}

@app.route("/")
def index():
    return render_template("index.html", libraries=[])

def get_libraries(str_libraries):
    library_list=str_libraries.split(",")
    libraries=[l.translate(extras).strip() for l in library_list if l.translate(extras).strip()]
    return libraries

@app.route("/add_library", methods=["POST"])
def add_library():
    libraries=get_libraries(request.form["libraries"])
    library=request.form["library"]
    if library and library not in libraries:
        libraries.append(library)
    return render_template("index.html", libraries=libraries)

@app.route("/delete_library", methods=["POST"])
def delete_library():
    library=request.form["library"]
    libraries=get_libraries(request.form["libraries"])
    libraries.remove(library)
    return render_template("index.html", libraries=libraries)

@app.route("/search", methods=["POST"])
def search():
    libraries=get_libraries(request.form["libraries"])
    if not libraries:
        return redirect("/")
    result=Search("/home/mizhonka/Documents/tbr.txt", libraries).check_availability()
    return render_template("results.html", links=result)

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

@app.route("/edit_piece/<int:id>")
def edit_piece(id):
    piece=pieces.get_by_id(id)
    piece_links=links.get_links(id)
    return render_template("piece_edit.html", piece=piece, piece_links=piece_links)

@app.route("/add_link", methods=["POST"])
def add_link():
    id=request.form["id"]
    link=request.form["link"]
    links.add(id, link)
    return redirect(f"/edit_piece/{id}")
