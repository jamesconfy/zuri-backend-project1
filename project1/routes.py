import json
from werkzeug.exceptions import HTTPException
from flask import current_app as app, make_response, request, abort


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
    response.access_control_allow_origin = "*"
    response.status_code = 200
    response.content_type = "application/json"

    return response

@app.route('/operation', methods=['POST'])
def operation():
    if request.method == 'POST' and request.is_json:
        opsList = ['addition', 'subtraction', 'multiplication']
        operand = request.json.get('operation_type')
        x = request.json.get('x')
        y = request.json.get('y')
        if operand in opsList:
            if operand == 'addition':
                result = x + y
            if operand == 'subtraction':
                result = x - y
            if operand == 'multiplication':
                result = x * y

            res = {
                "slackUsername": "everybody",
                "result": result,
                "operation_type": operand
            }

            response = make_response(res, 200)
            return response
        else:
            abort(400, description="Check the operation_type")

    else:
        abort(400, description="application/json is required!")


@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "message": e.description
    })
    response.content_type = "application/json"
    return response