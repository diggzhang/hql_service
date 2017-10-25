import os
import sys
from flask import Flask, request
from flask_restful import Resource, Api
from pyhive import hive

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from .utils import *
from config import *

cursor = hive.connect(host=HIVEURI, port=HIVEURIPORT).cursor()

app = Flask(__name__)
api = Api(app)


class Ping(Resource):
    def get(self):
        return {'ping': 'pong'}


class HqlCommander(Resource):
    def get(self):
        return {
            'hql': 'SELECT event_key as eventKey, d_app_version as appVersion FROM events.frontend_event_orc WHERE event_key = "whatKey" AND day = 20171024 LIMIT 3',
            'comment': 'POST /hql query example',
        }

    def post(self):
        req_json = request.get_json(force=True)
        hql_line = req_json['hql']
        results = hql_commander(cursor, hql_line)
        return {"hive_results": results}


class EventsCommander(Resource):
    def get(self):
        return {
            'appVersion': '4.1.0',
            'eventKey': 'enterHome',
            'userId': 'bacedecf23423144124214134',
            'comment': 'POST /event example'
        }

    def post(self):
        req_json = request.get_json(force=True)
        request_hql_element = {
            'appVersion': req_json['appVersion'],
            'eventKey': req_json['eventKey'],
            'userId': req_json['userId'],
            'day': query_day_is()
        }
        hql_query_line = hql_query_line_generator(request_hql_element)
        results = hql_commander(cursor, hql_query_line)
        return {"fieldsList": RETURN_FIELDS_LIST ,"results": results}


api.add_resource(Ping, '/')
api.add_resource(HqlCommander, '/hql')
api.add_resource(EventsCommander, '/event')


if __name__ == '__main__':
    app.run(host=SERVER_ADDR, port=SERVER_PORT, debug=ISDEBUG)
