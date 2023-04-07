from flask import Flask, request, render_template
from utils.request import generate_bio
import time 

app = Flask(__name__, template_folder="templates")

@app.route("/", methods=["GET", "POST"])
def main_get():
    if request.method == "GET":
        return render_template("main.html")
    else:
        personal_info = dict(request.form)
        #bio = generate_bio(**personal_info)
        bio = 'this is my bio \n Later more \n'.split('\n')
        time.sleep(5)

        return render_template('main.html', bio=bio)