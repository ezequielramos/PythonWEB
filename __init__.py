import sqlite3
from flask import Flask, request, render_template

#conn

conn = sqlite3.connect('test.db')
c = conn.cursor()

c.execute("SELECT name FROM sqlite_master WHERE type='table' AND NAME='users' ")

if not c.fetchone():
    c.execute("CREATE TABLE users(user text, password text)")

conn.close()

#form

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():

    user = request.args.get('user')
    password = request.args.get('pass')

    conn = sqlite3.connect('test.db')

    if user and password:
        c = conn.cursor()
        c.execute("INSERT INTO users (user, password) VALUES(?,?)",(user,password))
        conn.commit()

    conn.close()

    return render_template('index.html',user=user,password=password)

#list
@app.route('/list')
def list_users():

    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    conn.close()

    return render_template('list.html',users=users)

app.run()