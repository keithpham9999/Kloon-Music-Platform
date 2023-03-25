from flask import Flask, render_template, request, flash
from flask_socketio import SocketIO

from Database import Database




app = Flask(__name__)
app.config['SECRET_KEY'] = "secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kloon.db'
@app.route('/', methods=['POST', 'GET'])
def index():
    """Renders the home page
    """
    return render_template('home_page.html')

if __name__ == "__main__":
    app.run(debug=True, port=6969)
