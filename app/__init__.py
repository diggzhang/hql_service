from flask import Flask, request
from flask_restful import Resource, Api
from pyhive import presto

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
        return [{"hql_status": True}]


api.add_resource(Ping, '/')
api.add_resource(HqlCommander, '/hql')


if __name__ == '__main__':
    app.run(debug=True)
