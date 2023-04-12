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

        # email = dict(request.form)['e-mail']
        # info = scrape_profile(email)
        # bio = generate_bio(info)

        with open('bio.txt', 'r') as f:
            bio = f.read()
        
        first_name = 'luuk'
        second_name = 'hofman'

        bio = [part for part in bio.split('<br>') if len(part) > 1]
        time.sleep(2)
        elapsed_time = time.time() - start_time
        print(f'Total time elaped: {round(elapsed_time,2)} sec')
        return render_template('bio.html', bio=bio, first_name=first_name, last_name=second_name)
    
