from flask import Flask
from flask import render_template, request
from search import Search

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    books=request.files["books.txt"]
    libraries=request.form.getlist("top")
    available=Search(books, libraries).check_availability()
    if len(available)<=0:
        available=None
    return render_template("result.html", available=available)
