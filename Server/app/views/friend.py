from flasgger import swag_from
from flask import request
from flask_restful import Api

from app import friend_blueprint
from app.docs.friend import *
from app.views import BaseResource

api = Api(friend_blueprint)
api.prefix = '/friend'


@api.resource('/find')
class FindFriend(BaseResource):
    @swag_from(FIND_FRIEND_POST)
    def post(self):
        pass


@api.resource('/list')
class FriendList(BaseResource):
    @swag_from(FRIEND_LIST_GET)
    def get(self):
        pass
