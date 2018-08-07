from mongoengine import *


class UserModel(Document):
    meta = {
        'collection': 'user'
    }

    uuid = StringField(
        primary_key=True
    )

    name = StringField(
        required=True
    )
    age = IntField(
        required=True
    )
    sex = StringField(
        required=True
    )
    region = StringField(
        required=True
    )
    nickname = StringField(
        required=True
    )
    prefer_age = IntField(
        required=True
    )
    profile_image = StringField(
        default='default_profile.jpg'
    )
