from flask import Blueprint
from flask_restful import Api

from myapi.api.resources import UserResource, UserList, HomePage, HomePage2


blueprint = Blueprint('api', __name__)
api = Api(blueprint)


api.add_resource(UserResource, '/users/<int:user_id>')
api.add_resource(UserList, '/users')
api.add_resource(HomePage, '/home')
api.add_resource(HomePage2, '/')
