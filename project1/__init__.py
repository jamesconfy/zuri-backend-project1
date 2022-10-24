from flask import Flask

def create_app():
    app = Flask("project1")

    with app.app_context():
        from project1 import routes

    return app