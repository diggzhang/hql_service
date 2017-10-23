from flask import Flask, request
from flask_restful import Resource, Api
from pyhive import hive
from utils import hql_commander

cursor = hive.connect(host='10.8.8.21', port=10000).cursor()

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
        hql_line = req_json['sql']
        results = hql_commander(cursor, hql_line)
        return [{"hive_results": results}]


api.add_resource(Ping, '/')
api.add_resource(HqlCommander, '/hql')


if __name__ == '__main__':
    app.run(debug=True)
