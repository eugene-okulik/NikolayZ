import requests

BASE_URL = 'http://objapi.course.qa-practice.com'


def get_all_objects():
    response = requests.get(BASE_URL + '/object')
    print(response.json())


def get_one_objects(id):
    response = requests.get(BASE_URL + f'/object/{id}')
    print(response.json())


def post_object():
    body = {"name": 'Tesla', "data": {"car": "BMW", "carColor": "Black", "carNumber": "A123AA"}}
    response = requests.post(BASE_URL + '/object', json=body)
    print(response.json())
    assert response.status_code == 200
    assert response.json()['name'] == 'Tesla'


def put_object(id):
    body = {"name": 'Tesla', "data": {"car": "BMW", "carColor": "BLACK-White", "carNumber": "A123AA"}}
    response = requests.put(BASE_URL + f'/object/{id}', json=body)
    print(response.json())
    assert response.json()['data']['carColor'] == 'BLACK-White', 'carColor is not BLACK-White'


def patch_object(id):
    body = {"data": {"carColor": "White"}}
    response = requests.patch(BASE_URL + f'/object/{id}', json=body)
    print(response.json())
    assert response.json()['data']['carColor'] == 'White', 'carColor is not White'
    response = requests.get(BASE_URL + f'/object/{id}')
    print(response.json())
    assert response.json()['data']['car'] is not None, 'car is not Null'
    assert response.json()['data']['carNumber'] is not None, 'carNumber is not Null'


def delete_object(id):
    response = requests.delete(BASE_URL + f'/object/{id}')
    print(response.json())
    assert response.status_code == 200


post_object()
get_all_objects()
put_object(538)
get_one_objects(538)
patch_object(538)
get_one_objects(538)
delete_object(538)
