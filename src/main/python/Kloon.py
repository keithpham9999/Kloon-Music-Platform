import os

from flask import Flask, render_template, request, flash
from flask_socketio import SocketIO
import sqlite3
from flask_sqlalchemy import SQLAlchemy

from Database import Database


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret key"


@app.route('/loginPage/')
def login_page_redirect():
    """Loads login page
    """
    return render_template('login.html')

@app.route('/musicPage/', methods=["POST", "GET"])
def music_page_redirect():
    """Load music page
    """
    return render_template('music_page.html')


@app.route('/', methods=['POST', 'GET'])
def index():
    """Renders the home page
    """
    return render_template('home_page.html')

def add_music():
    """Adds music into database
    """
    music = Database()
    music.music_reset()
    music.close()


if __name__ == "__main__":
    add_music()
    app.run(debug=True, port=6969)
