import os

from flask import Flask, render_template, request, flash
from flask_socketio import SocketIO
import sqlite3
from flask_sqlalchemy import SQLAlchemy

from Database import Database


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret key"



@app.route('/', methods=['POST', 'GET'])
def index():
    """Renders the home page
    """
    return render_template('home_page.html')

def add_music():
    """Adds music into database
    """
    music = Database()
    music.create_music_tables()
    music.create_music_tables()
    music.fill_music()
    music.close()


if __name__ == "__main__":
    add_music()
    app.run(debug=True, port=6969)
