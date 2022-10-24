from flask import current_app as app

@app.route("/")
@app.route("/home")
def home():
    return "Hello World!"