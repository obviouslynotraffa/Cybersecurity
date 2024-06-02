import os
import sqlite3 as sql
from flask import Flask, render_template, make_response, request
from flask import redirect
from flask import session

app = Flask(__name__)

def retrieveUser(username, password):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute(f'SELECT id, username FROM `users` WHERE username=\'{username}\' AND password=\'{password}\'')
    user=cur.fetchone()
    con.commit()
    con.close()

    return {'id': user[0], 'username': user[1]} if user is not None else None


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        user=retrieveUser(username, password)
        if user==None:
            return render_template('index.html', nologin=[1])
        else:
            return render_template('flag.html')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')