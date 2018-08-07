MAIL_POST = {
    'tags': ['mail'],
    'description': '연서 보내기',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'api를 호출한 사람의 uuid',
            'in': 'header',
            'type': 'string',
            'required': True
        },
        {
            'name': 'receiver_id',
            'description': '수신자 uuid',
            'in': 'json',
            'type': 'string',
            'required': True
        },
        {
            'name': 'mail',
            'description': '연서 이미지 파일 이름',
            'in': 'json',
            'type': 'string',
            'required': True
        }
    ],

    'responses': {
        '201': {
            'description': '성공'
        },
        '204': {
            'description': '수신자 uuid 없음'
        },
        '401': {
            'description': 'api를 호출한 사람의 uuid 오류'
        }
    }
}

MAIL_LIST_GET = {
    'tags': ['mail'],
    'description': '연서 리스트 가져오기',
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
        '200': {
            'description': '성공',
            'example': [
                    {
                        'mail': '이미지 이름',
                        'sender': '보낸 사람의 이름',
                        'sender_id': '보낸 사람의 uuid'
                    },
                    {
                        'mail': '이미지 이름 ㅁㅁㅁ',
                        'sender': '보낸 사람의 이름 ㅁㅁㅁ',
                        'sender_id': '보낸 사람의 uuid ㅁㅁㅁ'
                    }                    
                ]
        },
        '204': {
            'description': '받은 연서가 없음'
        },
        '401': {
            'description': 'api를 호출한 사람의 uuid 오류'
        }
    }
}