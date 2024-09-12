from flask import Flask

import sqlite3

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def hello_world():
    return "<p>Hello, World! Syreen</p>"

@app.route("/list")
def get_list():
    return "<p>Here is your list</p>"


@app.route("/goodbye")
def goodbye():
    return "<p>Good Bye!</p>"