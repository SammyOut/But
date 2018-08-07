from flasgger import swag_from
from flask import request
from flask_restful import Api

from app import mail_blueprint
from app.docs.mail import *
from app.views import BaseResource

api = Api(mail_blueprint)
api.prefix = '/mail'


@api.resource('/')
class Mail(BaseResource):
    @swag_from(MAIL_POST)
    def post(self):
        pass

    @swag_from(MAIL_GET)
    def get(self):
        pass


@api.resource('/list')
class MailList(BaseResource):
    @swag_from(MAIL_LIST_GET)
    def get(self):
        pass
