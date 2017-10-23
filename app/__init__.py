import os
import sys
from flask import Flask, request
from flask_restful import Resource, Api
from pyhive import hive

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from utils import hql_commander
from config import *

cursor = hive.connect(host=HIVEURI, port=HIVEURIPORT).cursor()

app = Flask(__name__)
api = Api(app)

class Ping(Resource):
    def get(self):
        return {'ping': 'pong'}


class HqlCommander(Resource):
    def get(self):
        return {'hql': 'example'}

    def post(self):
        req_json = request.get_json(force=True)
        hql_line = req_json['hql']
        results = hql_commander(cursor, hql_line)
        return {"hive_results": results}


api.add_resource(Ping, '/')
api.add_resource(HqlCommander, '/hql')


if __name__ == '__main__':
    app.run(host=SERVER_ADDR, port=SERVER_PORT, debug=ISDEBUG)
