import os
import sys
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from pyhive import hive

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
CONFIG_MODULE = os.environ.get('HQL_SERVIECE_CONFIG', 'config')

from .utils import *

app = Flask(__name__)
CORS(app, supports_credentials=True)
api = Api(app)
app.config.from_object(CONFIG_MODULE)
conf = app.config

if conf.get('HIVEURI') and conf.get('HIVEURIPORT'):
    cursor = hive.connect(host=conf.get('HIVEURI'), port=conf.get('HIVEURIPORT')).cursor()

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
            'os': req_json['os'],
            'day': query_day_is()
        }
        hql_query_line = hql_query_line_generator(request_hql_element)
        query_results = hql_commander(cursor, hql_query_line)
        return convert_content_to_json(query_results)


api.add_resource(Ping, '/')
api.add_resource(HqlCommander, '/hql')
api.add_resource(EventsCommander, '/event')


if __name__ == '__main__':
    app.run(host=conf.get('HIVEURI'), port=conf.get('HIVEURIPORT'), debug=conf.get('ISDEBUG'))
