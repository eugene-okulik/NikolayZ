import allure


class Endpoint:
    url = 'http://objapi.course.qa-practice.com/object'
    response = None
    json = None
    headers = {'Content-Type': 'application/json'}

    @allure.step("Проверить, что ответ сервера имеет статус-код 200")
    def check_status_code_200(self):
        assert self.response.status_code == 200, "Status code is not 200"

    @allure.step("Проверить, что ответ сервера имеет статус-код 201")
    def check_status_code_201(self):
        assert self.response.status_code == 201, "Status code is not 201"

    @allure.step("Проверить, что ответ сервера имеет статус-код 400")
    def check_status_code_400(self):
        assert self.response.status_code == 400, "Status code is not 400"

    @allure.step("Проверить, что ответ сервера имеет статус-код 404")
    def check_status_code_404(self):
        assert self.response.status_code == 404, "Status code is not 404"

    @allure.step('Проверить, что имя в ответе совпадает с переданным')
    def check_name(self, name):
        assert self.json['name'] == name, "Name is not correct"

    @allure.step("Проверить, что цвет автомобиля обновился на ожидаемый")
    def check_carColor(self, expected_color):
        assert self.json['data']['carColor'] == expected_color, 'carColor is not correct"'

    @allure.step("Проверить, что ID в ответе совпадает с запрошенным")
    def check_id(self, object_id):
        assert self.response.json()['id'] == object_id, "ID is not correct"

    @allure.step("проверить наличие полей 'carColor', 'car', 'carNumber' и они не None")
    def check_fields(self):
        data = self.json.get('data', {})
        for field in ('carColor', 'car', 'carNumber'):
            assert data.get(field) is not None, (
                f"Поле '{field}' отсутствует или None. "
                f"Есть ключи: {list(data.keys())}. Полный ответ: {self.json}"
            )
