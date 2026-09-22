import pytest

NEW_CAR = [
    ("Tesla", {"car": "Tesla", "carColor": "black", "carNumber": "FF678YY"}),
    ("Toyota", {"car": "Toyota", "carColor": "white", "carNumber": "HJ873PK"}),
    ("Volvo", {"car": "Volvo", "carColor": "red", "carNumber": "KJ873PK"})
]

@pytest.mark.parametrize("name, data", NEW_CAR)
def test_post_object(create_object_endpoint, name, data):
    body = {"name": name, "data": data}

    create_object_endpoint.create_new_object(payload=body)
    create_object_endpoint.check_status_code_200()
    create_object_endpoint.check_name(body['name'])

def test_put_object(create_test_object, update_object_endpoint):
    body_update = {"name": 'Tesla', "data": {"car": "BMW", "carColor": "BLACK-White", "carNumber": "A123AA"}}

    update_object_endpoint.update_object(create_test_object, payload=body_update)
    update_object_endpoint.check_status_code_200()
    update_object_endpoint.check_name(body_update['name'])
    update_object_endpoint.check_carColor(body_update['data']['carColor'])

def test_get_all_objects(get_many_object_endpoint):
    get_many_object_endpoint.get_all_objects()
    get_many_object_endpoint.check_status_code_200()

def test_get_one_object(create_test_object, get_one_object_endpoint):
    get_one_object_endpoint.get_one_objects(create_test_object)
    get_one_object_endpoint.check_status_code_200()
    get_one_object_endpoint.check_id(create_test_object)
    get_one_object_endpoint.check_fields()

def test_patch_object(create_test_object, change_object_endpoint):
    body = {"data": {"carColor": "White"}}
    change_object_endpoint.update_object(create_test_object, payload=body)
    change_object_endpoint.check_status_code_200()
    change_object_endpoint.check_carColor(body['data']['carColor'])
    change_object_endpoint.check_fields()

def test_delete_object(create_test_object, delete_object_endpoint, get_one_object_endpoint):
    deleted_id = delete_object_endpoint.delete_object(create_test_object)
    delete_object_endpoint.check_status_code_200()
    get_one_object_endpoint.get_one_objects(deleted_id)
    get_one_object_endpoint.check_status_code_404()
