from flask_restful import Resource
from flask import jsonify
from database import get_client


class Index(Resource):
    def get(self):
        return {'hello': 'world'}
    
    
class Heartbeat(Resource):
    def get(self):
        client = get_client()
        return jsonify({"mongodb connection test": client.test.command('dbstats')})
