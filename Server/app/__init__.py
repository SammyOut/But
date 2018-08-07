from flask import Blueprint, Flask
from flasgger import Swagger

from mongoengine import connect

from app.views import route

api_v1_blueprint = Blueprint('api', __name__)


def create_app(*config_cls) -> Flask:
    print('[INFO] Flask application initialized with {}'.format([config.__name__ for config in config_cls]))

    app_ = Flask(__name__)

    for config in config_cls:
        app_.config.from_object(config)

    Swagger(template=app_.config['SWAGGER_TEMPLATE']).init_app(app_)

    connect(**app_.config['MONGODB_SETTINGS'])
    route(app_)

    return app_
