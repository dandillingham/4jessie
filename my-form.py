from flask import Flask
from flask import request
from flask import render_template
import stringComparison

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("index.html") # this should be the name of your html file

@app.route('/', methods=['POST'])
def my_form_post():

    first_name = request.form['fname']
    last_name = request.form['lname']
    date_of_birth = request.form['dob']

    print (request.form)

    return "<h1>Data submitted!</h1>"

if __name__ == '__main__':
    app.run()
