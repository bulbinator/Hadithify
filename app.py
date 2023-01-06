import os
import requests

from flask import Flask, flash, redirect, render_template, request

from functions import get_hadith

app = Flask(__name__)


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        hadith = get_hadith()
        arabic = hadith["arabic"]
        english = hadith["english"]
        author = hadith["author"]
        book = hadith["book"]
        url = hadith["URL"]
        return render_template("index.html", arabic=arabic, english=english, author=author, book=book, url=url)
    else:
        hadith = get_hadith()
        arabic = hadith["arabic"]
        english = hadith["english"]
        author = hadith["author"]
        book = hadith["book"]
        url = hadith["URL"]
        return render_template("index.html", arabic=arabic, english=english, author=author, book=book, url=url)


