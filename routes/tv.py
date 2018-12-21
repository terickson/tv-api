import json
from flask import Blueprint, current_app, Response, request
from pprint import pprint
from time import sleep

roku_template = Blueprint('tv_template', __name__, template_folder='templates')


@tv_template.route('/actions', methods=['POST'])
def actions():
    return create_action()


def create_action():
    current_app.logger.info("post tv action")
    tvInfo = request.json
    if 'comand' not in tvInfo:
        return Response(json.dumps({"message": "attribute comand must be passed"}), status=412, mimetype='application/json')
    if 'value' in tvInfo:
        getattr(current_app.tv, tvInfo.get('comand'))(tvInfo.get('value'))
    else:
        getattr(current_app.tv, tvInfo.get('comand'))()
    return Response(json.dumps({"message": "success"}), status=201, mimetype='application/json')
