SIGNUP_POST = {
    'tags': ['signup'],
    'description': '회원 정보 등록',
    'parameters': [
        {
            'name': 'name',
            'description': '이름',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'age',
            'description': '나이',
            'in': 'json',
            'type': 'int',
            'required': True
        },
        {
            'name': 'sex',
            'description': '성별',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'region',
            'description': '지역',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'profile_image',
            'description': '프로필 사진 이름',
            'in': 'json',
            'type': 'string',
            'required': False
        }
    ],
    'responses': {
        '201': {
            'description': '성공',
            'example': {
                'user_id': '유저uuid'
            }
        }
    }
}