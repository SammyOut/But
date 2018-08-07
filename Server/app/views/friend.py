from flasgger import swag_from
from flask import request, abort, Response
from flask_restful import Api

from random import shuffle

from app import friend_blueprint
from app.docs.friend import *
from app.models.user import UserModel
from app.models.friend import FriendModel
from app.views import BaseResource

api = Api(friend_blueprint)
api.prefix = '/friend'


@api.resource('/find')
class FindFriend(BaseResource):
    @swag_from(FIND_FRIEND_POST)
    def post(self):
        user = UserModel.objects(uuid=request.headers['Authorization']).first()
        if not user:
            abort(401)

        payload = request.json

        if payload['region']:
            people = UserModel.objects(region=user.region)
        else:
            people = UserModel.objects()

        result = [{
            'id': person.uuid,
            'name': person.name,
            'profile_image': person.profile_image,
            'region': person.region,
            'age': person.age
        } for person in people]
        shuffle(result)

        return self.unicode_safe_json_dumps(result[:payload['count']])


@api.resource('/list')
class FriendList(BaseResource):
    @swag_from(FRIEND_LIST_GET)
    def get(self):
        user = UserModel.objects(uuid=request.headers['Authorization']).first()
        if not user:
            abort(401)

        friend = FriendModel.objects(user=user).first()
        if not friend:
            return Response('', 204)

        result = [{
            'id': friend.uuid,
            'name': friend.name,
            'profile_image': friend.profile_image,
            'region': friend.region,
            'age': friend.age
        }for friend in friend.friend]

        return self.unicode_safe_json_dumps(result)
