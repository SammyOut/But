FIND_FRIEND_POST = {
    'tags': ['friend'],
    'description': '벗 찾기',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'api를 호출한 사람의 uuid',
            'in': 'header',
            'type': 'string',
            'required': True
        },
        {
            'name': 'region',
            'description': '본인 지역과 같은 벗을 검색할 것인가',
            'in': 'json',
            'type': 'bool',
            'required': True
        },
        {
            'name': 'age',
            'description': '본인 희망 연령대를 검색할 것인가',
            'in': 'json',
            'type': 'bool',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '성공',
            'examples': [{
                        'name': '이름',
                        'profile_image': '프로필 사진',
                        'id': 'uuid'
                    },
                    {
                        'name': '이름 ㅁㅁㅁ',
                        'profile_image': '프로필 사진 ㅁㅁㅁ',
                        'id': 'uuid ㅁㅁㅁ'
                    }
                ]
        },
        '204': {
            'description': '검색 결과 없음'
        },
        '401': {
            'description': 'api를 호출한 사람의 uuid 오류'
        }
    }
}

FRIEND_LIST_GET = {
    'tags': ['friend'],
    'description': '벗 리스트 조회',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'api를 호출한 사람의 uuid',
            'in': 'header',
            'type': 'string',
            'required': True
        }
    ],

    'responses': {
        '201': {
            'description': '성공',
            'examples': [{
                        'name': '이름',
                        'profile_image': '프로필 사진',
                        'id': 'uuid'
                    },
                    {
                        'name': '이름 ㅁㅁㅁ',
                        'profile_image': '프로필 사진 ㅁㅁㅁ',
                        'id': 'uuid ㅁㅁㅁ'
                    }
                ]
        },
        '204': {
            'description': '검색 결과 없음'
        },
        '401': {
            'description': 'api를 호출한 사람의 uuid 오류'
        }
    }
}