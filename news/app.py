
from flask import Flask, render_template
import sqlite3
import requests 
from flask_sqlalchemy import SQLAlchemy


applicat = Flask(__name__)





def get_db_connection():
    conn = sqlite3.connect('database3.db')
    conn.row_factory = sqlite3.Row
    return conn

@applicat.route('/')
def index():
    conn = get_db_connection()
    newss = conn.execute('SELECT * FROM yemennews').fetchall()
    conn.close()
    return render_template('index.html', news=newss)


