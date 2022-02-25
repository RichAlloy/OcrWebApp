from flask import Blueprint, render_template, request, flash, redirect, url_for
from .ocr_translator import image_text, translate

views = Blueprint('views', __name__)

@views.route("/", methods=["GET","POST"])
@views.route("/home")
def home():
    return render_template('index.html')

@views.route("/upload", methods=["GET","POST"])
def upload():
    if request.method == "POST":

        url = request.form.get('url')
        langs = request.form.get('langs')
        text = image_text(url, langs)
        translation = translate(text, langs)
        # print(url)


        return render_template("upload.html", url=url, text=text, translation=translation)

    return render_template("upload.html")

