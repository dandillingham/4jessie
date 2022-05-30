from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__, template_folder=".")

@app.route('/')
def my_form():
    return render_template("index.html")   # this should be the name of your html file

@app.route('/', methods=['POST'])
def my_form_post():

    first_name = request.form['fname']
    last_name = request.form['lname']
    date_of_birth = request.form['dob']

    print (first_name, flush=True)
    print (last_name, flush=True)
    print (date_of_birth, flush=True)
    print (request.form, flush=True)

    return "<h1>Form submitted!</h1>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
