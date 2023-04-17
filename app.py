import time 
import logging
from flask import Flask, request, render_template
from utils.request import generate_bio
from utils.request import scrape_profile

app = Flask(__name__, template_folder="templates")

@app.route("/", methods=["GET", "POST"])
def main_get():
    if request.method == "GET":
        app.logger.info('A user connected to the app!')
        return render_template("email.html")
    else:
        start_time = time.time()
    
    try:
        if app.debug:
            with open('./utils/debug_bio.txt', 'r') as f:
                bio = f.read()
                first_name = 'John'
                last_name = 'Doe'
                time.sleep(2)

        else:
            email = dict(request.form)['e-mail']
            info = scrape_profile(email)
            bio = generate_bio(info)
            first_name = info['header']['first_name']
            last_name = info['header']['last_name']

        bio = [part for part in bio.split('<br>') if len(part) > 1]
        elapsed_time = time.time() - start_time
        app.logger.info(f'Bio generated in - {round(elapsed_time,2)} sec.')
        return render_template('bio.html', bio=bio, first_name=first_name, last_name=last_name)
    
    except Exception as e:
        app.logger.exception(f'There was an error - {e}')
        return render_template('error.html', exception=e)

if __name__ == '__main__':
    app.run(host='0.0.0.0')