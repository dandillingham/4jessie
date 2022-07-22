from flask import Flask
from flask import request
from flask import render_template
import sqlite3

app = Flask(__name__, template_folder=".")

@app.route('/')
def my_form():
    return render_template("index.html")   # this should be the name of your html file

@app.route('/', methods=['POST'])
def my_form_post():

    connection = sqlite3.connect('people.db')
    cursor = connection.cursor()

    my_form = request.form['my-form']

    if my_form == "Insert":
        do_insert(cursor, request.form)
    
    connection.commit()
    connection.close()

    print (request.form, flush=True)
    return "<h1>Form submitted!</h1>"

def do_insert(cursor, form):

    cursor.execute("select max(id) from person")
    tempid = cursor.fetchall()
    if tempid[0][0] == None:
        rowid = 1
    else:
        rowid = int(tempid[0][0])+1

    first_name    = form['fname']
    last_name     = form['lname']
    date_of_birth = form['dob']
    mummy         = form['mummy']
    daddy         = form['daddy']

    cursor.execute("INSERT INTO person VALUES (?, ?, ?, ?, ?, ?)", (rowid, first_name, last_name, date_of_birth, mummy, daddy))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
