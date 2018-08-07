from flasgger import swag_from
from flask import request
from flask_restful import Api

from uuid import uuid4

from app import signup_blueprint
from app.docs.signup import *
from app.models.user import UserModel
from app.views import BaseResource

api = Api(signup_blueprint)
api.prefix = '/signup'


@api.resource('/')
class Signup(BaseResource):
    @swag_from(SIGNUP_POST)
    def post(self):
        payload = request.json
        uuid = uuid4()
        payload['uuid'] = uuid

        UserModel(**payload).save()

        return self.unicode_safe_json_dumps({'user_id': uuid}, 201)
