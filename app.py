from flask import Flask, request
from flask import render_template
from utils.request import generate_bio

app = Flask(__name__, template_folder="templates")

@app.route("/", methods=["GET", "POST"])
def main_get(name=None):
    if request.method == "GET":
        return render_template("main.html")
    else:
        personal_info = dict(request.form)
        bio = generate_bio(**personal_info)
        return render_template("main.html", bio=bio)
    