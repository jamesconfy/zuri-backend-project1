from flask import current_app as app, jsonify

@app.route("/")
@app.route("/home")
def home():
    return jsonify("Hello World!")