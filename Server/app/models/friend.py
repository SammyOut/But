from mongoengine import *

from app.models.user import UserModel


class FriendModel(Document):
    user = ReferenceField(
        document_type=UserModel
    )

    friend = ListField(
        ReferenceField(
            document_type=UserModel
        ),
        default=[]
    )
