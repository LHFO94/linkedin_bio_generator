from flask import Flask, request, render_template
from utils.request import generate_bio
from utils.request import scrape_profile
import time 

app = Flask(__name__, template_folder="templates")

@app.route("/", methods=["GET", "POST"])
def main_get():
    if request.method == "GET":
        return render_template("email.html")
    else:
        start_time = time.time()
        
        if app.debug:
            with open('./utils/debug_bio.txt', 'r') as f:
                bio = f.read()
                first_name = 'John'
                second_name = 'Doe'
                time.sleep(2)

        else:
            email = dict(request.form)['e-mail']
            info = scrape_profile(email)
            bio = generate_bio(info)
 
        bio = [part for part in bio.split('<br>') if len(part) > 1]
        elapsed_time = time.time() - start_time
        app.logger.info(f'Bio generated in - {round(elapsed_time,2)} - sec.')
        return render_template('bio.html', bio=bio, first_name=first_name, last_name=second_name)