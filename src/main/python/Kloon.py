from flask import Flask, render_template, request, flash
from flask_socketio import SocketIO


# import api and client modules
from api.api import api_blueprint
from client.client import client_blueprint