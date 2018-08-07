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
    profile_image = StringField(
        default='default_profile.jpg'
    )
