from flasgger import swag_from
from flask import request, abort, Response
from flask_restful import Api

from app import mail_blueprint
from app.docs.mail import *
from app.models.mail import MailModel
from app.models.user import UserModel
from app.views import BaseResource

api = Api(mail_blueprint)
api.prefix = '/mail'


@api.resource('/')
class Mail(BaseResource):
    @swag_from(MAIL_POST)
    def post(self):
        pass


@api.resource('/list')
class MailList(BaseResource):
    @swag_from(MAIL_LIST_GET)
    def get(self):
        user = UserModel.objects(uuid=request.headers['Authorization']).first()
        mails = MailModel.objects.filter(Q(sender=user) or Q(receiver=user))

        if not user:
            abort(401)

        if not mails:
            return Response('', 204)

        result = [{
            'mail': mail.image,
            'sender': mail.sender.name,
            'sender_id': mail.sender.uuid
        }for mail in mails]

        return self.unicode_safe_json_dumps(result)