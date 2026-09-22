import requests
import allure
from endpoints.endpoint import Endpoint


class GetOneObject(Endpoint):
    @allure.step("Отправить GET-запрос на Получение одного объекта по ID/object")
    def get_one_objects(self, object_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(f'{self.url}/{object_id}', headers=headers)

        try:
            self.json = self.response.json()
        except requests.exceptions.JSONDecodeError:
            self.json = None  # ← 404 с HTML-телом: json просто None (при удалении объекта)
        return self.response, self.json
