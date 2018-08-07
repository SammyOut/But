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
        """
        연서 보내기
        """
        user = UserModel.objects(uuid=request.headers['Authorization']).first()
        if not user:
            abort(401)

        receiver = UserModel.objects(uuid=request.json['receiver_id']).first()
        if not receiver:
            return Response('', 204)

        MailModel(
            sender=user,
            receiver=receiver,
            mail=request.json['mail']
        ).save()

        return Response('', 201)

    @swag_from(MAIL_LIST_GET)
    def get(self):
        """
        연서 목록 가져오기
        """
        user = UserModel.objects(uuid=request.headers['Authorization']).first()
        mails = MailModel.objects(receiver=user)

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
