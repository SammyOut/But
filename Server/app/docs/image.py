IMAGE_POST = {
    'tags': ['image'],
    'description': '이미지 저장하기',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'api를 호출한 사람의 uuid',
            'in': 'header',
            'type': 'string',
            'required': True
        },
        {
            'name': 'image',
            'description': '이미지',
            'in': 'file',
            'type': 'image',
            'required': True
        }
    ],

    'responses': {
        '201': {
            'description': '성공',
            'example': {
                'image_name': '이미지 이름'
            }
        },
        '401': {
            'description': 'api를 호출한 사람의 uuid 오류'
        }
    }
}

IMAGE_GET = {
    'tags': ['image'],
    'description': '이미지 로드하기',
    'parameters': [
        {
            'name': 'image_name',
            'description': '이미지 이름',
            'in': 'query params',
            'type': 'string',
            'required': True
        }
    ],

    'responses': {
        '200': {
            'description': '성공 그리고 이미지 줄거야'
        },
        '204': {
            'description': '이미지 없음'
        }
    }
}