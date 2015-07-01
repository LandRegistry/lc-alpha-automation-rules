from application import app
from flask import Response
import logging
import json


@app.route('/', methods=["GET"])
def index():
    return Response(status=200)


@app.route('/check_auto', methods=['POST'])
def check_auto():
    logging.info("check_auto")

    auto = app.config['AUTOMATION_IND']

    if auto:
        data = {
            "register_auto": True
        }
    else:
        data = {
            "register_auto": False
        }

    return Response(json.dumps(data), status=200, mimetype='application/json')

