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

    auto_ind = app.config['AUTOMATION_IND']

    data = {
        "register_auto": auto_ind
    }

    return Response(json.dumps(data), status=200, mimetype='application/json')
