import os
import socket


class Config:
    SERVICE_NAME = 'But'
    SERVICE_NAME_UPPER = SERVICE_NAME.upper()
    REPRESENTATIVE_HOST = 'ec2.istruly.sexy'

    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 604
    DEBUG = False

    RUN_SETTING = {
        'threaded': True,
        'host': HOST,
        'port': PORT,
        'debug': DEBUG
    }

    MONGODB_SETTINGS = {
        'db': SERVICE_NAME
    }

    SWAGGER = {
        'title': SERVICE_NAME,
        'specs_route': os.getenv('SWAGGER_URI', '/docs'),
        'uiversion': 3,

        'info': {
            'title': SERVICE_NAME + ' API',
            'version': '1.0',
            'description': ''
        },
        'basePath': '/ ',
        'host': '{}:{}'. format(REPRESENTATIVE_HOST or HOST, PORT)
    }

    SWAGGER_TEMPLATE = {
        'schemes': [
            'http'
        ],
        'tags': [
            {
                'name': 'Some Tag',
                'description': 'Some API'
            },
        ]
    }
