import requests
import allure
from endpoints.endpoint import Endpoint


class GetManyObject(Endpoint):
    @allure.step("Отправить GET-запрос на получение списка объектов /object")
    def get_all_objects(self, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(f'{self.url}', headers=headers)
        self.json = self.response.json()
        return self.response, self.json
