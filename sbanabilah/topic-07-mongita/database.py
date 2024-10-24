from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from pprint import pprint

app = Flask(__name__)
connection = sqlite3.connect("pets.db", check_same_thread=False)
connection.execute("PRAGMA foreign_keys = 1")

def retrieve_list():
    cursor = connection.cursor()
    cursor.execute("""
        SELECT id, name, age, owner FROM pets 
    """)
    rows = cursor.fetchall()
    return rows
    #return render_template("list.html", rows=rows)
\
# def test_retrive_list():

def retrieve_kinds():
    cursor = connection.cursor()
    cursor.execute("""
        SELECT kind_name, food, noise FROM kind 
    """)
    kinds = cursor.fetchall()
    return kinds
