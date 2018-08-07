from flasgger import swag_from
from flask import request, Response, send_from_directory, abort
from flask_restful import Api

from app import mail_blueprint
from app.docs.image import *
from app.views import BaseResource

import os
from werkzeug.utils import secure_filename


api = Api(mail_blueprint)
api.prefix = '/image'

UPLOAD_FOLDER = 'static/upload'


@api.resource('/')
class Image(BaseResource):
    @swag_from(IMAGE_GET)
    def get(self, image_name):
        if not request.headers['Authorization']:
            abort(401)
        return send_from_directory(UPLOAD_FOLDER, image_name)

    @swag_from(IMAGE_POST)
    def post(self):
        image = request.files['image']
        image_name = secure_filename(image.filename)
        image.save(os.path.join(UPLOAD_FOLDER), image_name)
        return Response('', 201)
