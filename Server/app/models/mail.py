from mongoengine import *

from app.models.user import UserModel


class MailModel(Document):
    meta = {
        'collection': 'mail'
    }

    sender = ReferenceField(
        document_type=UserModel,
        required=True
    )
    image = StringField(
        required=True
    )
    receiver = ReferenceField(
        document_type=UserModel,
        required=True
    )
