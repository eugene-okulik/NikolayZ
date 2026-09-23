import pytest
import requests
from endpoints.create_object import CreateObject
from endpoints.update_object import UpdateObject
from endpoints.get_many import GetManyObject
from endpoints.get_one import GetOneObject
from endpoints.change_object import ChangeObject
from endpoints.delete_object import DeleteObject


@pytest.fixture()
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def update_object_endpoint():
    return UpdateObject()


@pytest.fixture()
def create_test_object(create_object_endpoint):
    body_test = {"name": "Test", "data": {"car": "Test_car", "carColor": "Test_color", "carNumber": "Test_number"}}
    create_object_endpoint.create_new_object(payload=body_test)
    test_id = create_object_endpoint.json['id']
    print(f"\n  → Создан объект с ID: {test_id}")
    yield test_id
    url = f'{create_object_endpoint.url}/object/{test_id}'
    headers = create_object_endpoint.headers
    check = requests.get(url, headers=headers)
    if check.status_code == 200:
        requests.delete(url, headers=headers)
        print(f'✓ Объект {test_id} удалён')
    else:
        print(f'! Объект {test_id} уже был удалён')


@pytest.fixture()
def get_many_object_endpoint():
    return GetManyObject()


@pytest.fixture()
def get_one_object_endpoint():
    return GetOneObject()


@pytest.fixture()
def change_object_endpoint():
    return ChangeObject()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()
