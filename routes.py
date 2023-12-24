from app import app
from flask import render_template, request
from search import Search

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
    if library:
        libraries.append(library)
    return render_template("index.html", libraries=libraries)

@app.route("/search", methods=["POST"])
def search():
    libraries=get_libraries(request.form["libraries"])
    print(libraries)
    result=Search("/home/mizhonka/Documents/tbr.txt", libraries).check_availability()
    return render_template("results.html", links=result)

