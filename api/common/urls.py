from api.common.views import Index, Heartbeat
from flask import Blueprint
from flask_restful import Api

common_blueprint = Blueprint('common', __name__)
common_urls = Api(common_blueprint)

# url schema
common_urls.add_resource(Index, '/')
common_urls.add_resource(Heartbeat, '/heartbeat')
