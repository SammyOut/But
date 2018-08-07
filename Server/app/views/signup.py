from flasgger import swag_from
from flask import request
from flask_restful import Api

from app import signup_blueprint
from app.docs.signup import *
from app.views import BaseResource

api = Api(signup_blueprint)
api.prefix = '/signup'


@api.resource('/')
class Signup(BaseResource):
    @swag_from(SIGNUP_POST)
    def post(self):
        pass
