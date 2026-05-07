import requests
import pytest

BASE_URL = 'http://objapi.course.qa-practice.com'
HEADERS = {'Content-Type': 'application/json'}

NEW_CAR = [
    ("Tesla", {"car": "Tesla", "carColor": "black", "carNumber": "FF678YY"}),
    ("Toyota", {"car": "Toyota", "carColor": "white", "carNumber": "HJ873PK"}),
    ("Volvo", {"car": "Volvo", "carColor": "red", "carNumber": "KJ873PK"})
]


@pytest.fixture(scope='session')
def start_all():
    print('\nStart testing')
    yield
    print('Testing completed')


@pytest.fixture()
def start_one():
    print("\nbefore test")
    yield
    print("\nafter test")


@pytest.fixture()
def create_test_object():
    body = {"name": "Test", "data": {"car": "Test_car", "carColor": "Test_color", "carNumber": "Test_number"}}
    response = requests.post(BASE_URL + '/object', json=body, headers=HEADERS)
    assert response.status_code == 200
    post_id = response.json()['id']
    print(f"\n  → Создан объект с ID: {post_id}")
    yield post_id
    check = requests.get(f'{BASE_URL}/object/{post_id}')
    if check.status_code == 200:
        delete_response = requests.delete(f'{BASE_URL}/object/{post_id}')
        assert delete_response.status_code == 200
        print(f'✓ Объект {post_id} удалён')
    else:
        print(f'! Объект {post_id} уже был удалён')


@pytest.mark.medium
def test_get_all_objects(start_all, start_one):
    response = requests.get(BASE_URL + '/object', headers=HEADERS)
    assert response.status_code == 200
    print(response.json())


def test_get_one_objects(start_one, create_test_object):
    post_id = create_test_object
    response = requests.get(BASE_URL + f'/object/{post_id}', headers=HEADERS)
    assert response.status_code == 200
    print(response.json())


@pytest.mark.critical
@pytest.mark.parametrize("name, data", NEW_CAR)
def test_post_object(name, data):
    body = {"name": name, "data": data}
    response = requests.post(BASE_URL + '/object', json=body, headers=HEADERS)
    assert response.status_code == 200
    assert response.json()['name'] == name, "Name is not correct"
    print(response.json())


def test_put_object(start_one, create_test_object):
    post_id = create_test_object
    body = {"name": 'Tesla', "data": {"car": "BMW", "carColor": "BLACK-White", "carNumber": "A123AA"}}
    response = requests.put(BASE_URL + f'/object/{post_id}', json=body)
    print(response.json())
    assert response.json()['data']['carColor'] == 'BLACK-White', 'carColor is not BLACK-White'


def test_patch_object(start_one, create_test_object):
    post_id = create_test_object
    body = {"data": {"carColor": "White"}}
    response = requests.patch(BASE_URL + f'/object/{post_id}', json=body)
    print(response.json())
    assert response.json()['data']['carColor'] == 'White', 'carColor is not White'
    response = requests.get(BASE_URL + f'/object/{post_id}')
    print(response.json())
    assert response.json()['data']['car'] is not None, 'car is not Null'
    assert response.json()['data']['carNumber'] is not None, 'carNumber is not Null'


def test_delete_object(start_one, create_test_object):
    post_id = create_test_object
    delete_response = requests.delete(f'{BASE_URL}/object/{post_id}')
    assert delete_response.status_code == 200
    print(f"\n  → Объект {post_id} удалён в тесте")
    get_response = requests.get(f'{BASE_URL}/object/{post_id}')
    assert get_response.status_code == 404
    print(f"  ✓ Подтверждено: объект {post_id} не найден")
