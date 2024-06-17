from flask import Flask
import spotipy

def create_app():
    app = Flask(__name__)
    return app