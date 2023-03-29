from flask import Flask, request
from flask import render_template

app = Flask(__name__, template_folder="templates")


@app.route("/", methods=["GET", "POST"])
def main_get(name=None):
    if request.method == "GET":
        print("foo")
        return render_template("main.html", name=name)
    else:
        email = request.form["email"]
        name = request.form["password"]
