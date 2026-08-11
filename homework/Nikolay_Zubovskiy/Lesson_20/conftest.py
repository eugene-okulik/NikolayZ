import pytest
import requests


BASE_URL = 'http://objapi.course.qa-practice.com'
HEADERS = {'Content-Type': 'application/json'}


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
    post_id = response.json()['id']
    print(f"\n  → Создан объект с ID: {post_id}")
    yield post_id
    check = requests.get(f'{BASE_URL}/object/{post_id}')
    if check.status_code == 200:
        requests.delete(f'{BASE_URL}/object/{post_id}', headers=HEADERS)
        print(f'✓ Объект {post_id} удалён')
    else:
        print(f'! Объект {post_id} уже был удалён')
