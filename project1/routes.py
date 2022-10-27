from flask import current_app as app, make_response

@app.route("/")
@app.route("/home")
def home():
    res = { 
            "slackUsername": "everybody", 
            "backend": True, 
            "age": 24, 
            "bio": "I am a self-taught programmer with experience working with Python, Flask, React, Docker and knowledge with hosting on AWS and Google Cloud Platform. I am a motivated person that picks up technologies easily"
    }
    
    response = make_response(res)
    response.status_code = 200
    response.content_type = "application/json"

    return response