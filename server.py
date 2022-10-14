#Framework: Flask, django
#python http.server

#To make custom virtual environment folder
#python3 -m venv YourFolderName/

from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

#Flask requires javascripts, CSS, img files, etc. to put in 'static' folder
#while htmls in 'templates' folder

#run expoert FLASK_APP=server.py
#export FLASK_DEBUG=True
#run flask run

#decorator
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Fail to save to database'
    else:
        return 'Something went wrong, please try again later.'
    
def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')
        
def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])        