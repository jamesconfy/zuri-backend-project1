from flask import Flask
from flask_cors import CORS

cors = CORS()

def create_app():
    app = Flask("project1")
    cors.init_app(app, resources="*")

    with app.app_context():
        from project1 import routes

    return app