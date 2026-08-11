import requests
import pytest
import allure
import json

BASE_URL = 'http://objapi.course.qa-practice.com'
HEADERS = {'Content-Type': 'application/json'}

NEW_CAR = [
    ("Tesla", {"car": "Tesla", "carColor": "black", "carNumber": "FF678YY"}),
    ("Toyota", {"car": "Toyota", "carColor": "white", "carNumber": "HJ873PK"}),
    ("Volvo", {"car": "Volvo", "carColor": "red", "carNumber": "KJ873PK"})
]


@allure.feature("Управление объектами")
@allure.story("Получение списка всех объектов")
@allure.title("Проверка получения всех объектов")
@pytest.mark.medium
def test_get_all_objects(start_all, start_one):
    with allure.step("Отправить GET-запрос на /object"):
        response = requests.get(BASE_URL + '/object', headers=HEADERS)
        allure.attach(
            json.dumps(response.json(), indent=2),
            name="Ответ сервера (все объекты)",
            attachment_type=allure.attachment_type.JSON
        )
    with allure.step("Проверить, что статус-код равен 200"):
        assert response.status_code == 200


@allure.feature("Управление объектами")
@allure.story("Получение одного объекта по ID")
@allure.title("Проверка получения существующего объекта")
def test_get_one_objects(start_one, create_test_object):
    post_id = create_test_object

    with allure.step(f"Отправить GET-запрос к /object/{post_id}"):
        response = requests.get(BASE_URL + f'/object/{post_id}', headers=HEADERS)
        allure.attach(
            json.dumps(response.json(), indent=2),
            name="Ответ сервера (объект)",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("Проверить статус-код ответа"):
        assert response.status_code == 200

    with allure.step("Проверить, что ID в ответе совпадает с запрошенным"):
        assert response.json()['id'] == post_id


@allure.feature("Управление объектами")
@allure.story("Создание нового объекта")
@pytest.mark.critical
@pytest.mark.parametrize("name, data", NEW_CAR)
def test_post_object(name, data, start_one):
    allure.dynamic.title(f"Создание объекта с именем '{name}' и данными {data}")

    body = {"name": name, "data": data}

    with allure.step(f"Отправить POST-запрос на /object с name='{name}'"):
        response = requests.post(BASE_URL + '/object', json=body, headers=HEADERS)
        allure.attach(
            json.dumps(response.json(), indent=2),
            name="Ответ сервера (созданный объект)",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("Проверить статус-код ответа"):
        assert response.status_code == 200

    with allure.step("Проверить, что имя в ответе совпадает с переданным"):
        assert response.json()['name'] == name, "Name is not correct"


@allure.feature("Управление объектами")
@allure.story("Полное обновление объекта (PUT)")
@allure.title("Обновление объекта через PUT-запрос")
def test_put_object(start_one, create_test_object):
    post_id = create_test_object
    body = {"name": 'Tesla', "data": {"car": "BMW", "carColor": "BLACK-White", "carNumber": "A123AA"}}

    with allure.step(f"Отправить PUT-запрос на /object/{post_id} с новыми данными"):
        response = requests.put(BASE_URL + f'/object/{post_id}', json=body)
        allure.attach(
            json.dumps(response.json(), indent=2),
            name="Ответ сервера (PUT)",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("Проверить статус-код ответа"):
        assert response.status_code == 200

    with allure.step("Проверить, что цвет обновился на 'BLACK-White'"):
        assert response.json()['data']['carColor'] == 'BLACK-White', 'carColor is not BLACK-White'


@allure.feature("Управление автомобилями")
@allure.story("Частичное обновление данных (PATCH)")
@allure.title("Обновление цвета автомобиля через PATCH")
def test_patch_object(start_one, create_test_object):
    post_id = create_test_object
    body = {"data": {"carColor": "White"}}

    with allure.step("Отправить PATCH-запрос на обновление цвета"):
        response = requests.patch(BASE_URL + f'/object/{post_id}', json=body)
        allure.attach(
            json.dumps(response.json(), indent=2),
            name="Ответ PATCH",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("Проверить, что цвет стал 'White'"):
        assert response.json()['data']['carColor'] == 'White', 'carColor is not White'

    with allure.step("Получить объект через GET и проверить наличие полей 'car', 'carNumber' и они не None"):
        response = requests.get(BASE_URL + f'/object/{post_id}')
        allure.attach(
            json.dumps(response.json(), indent=2),
            name="Ответ GET",
            attachment_type=allure.attachment_type.JSON
        )
        assert response.json()['data']['car'] is not None, 'car is not Null'
        assert response.json()['data']['carNumber'] is not None, 'carNumber is not Null'


@allure.feature("Управление объектами")
@allure.story("Удаление объекта")
@allure.title("Удаление существующего объекта")
def test_delete_object(start_one, create_test_object):
    post_id = create_test_object

    with allure.step(f"Удалить объект с ID = {post_id}"):
        delete_response = requests.delete(f'{BASE_URL}/object/{post_id}')

    with allure.step("Проверить, что удаление прошло успешно (статус 200)"):
        assert delete_response.status_code == 200
        print(f"\n  → Объект {post_id} удалён в тесте")

    with allure.step(f"Проверить, что объект {post_id} больше не существует"):
        get_response = requests.get(f'{BASE_URL}/object/{post_id}')

    with allure.step("Убедиться, что сервер вернул 404 (Not Found)"):
        assert get_response.status_code == 404
        print(f"  ✓ Подтверждено: объект {post_id} не найден")
