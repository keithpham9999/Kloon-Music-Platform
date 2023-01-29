from flask import Flask, render_template, request, flash
from flask_socketio import SocketIO





app = Flask(__name__)
if __name__ == "__main__":
    app.run(debug=True, port=6969)
