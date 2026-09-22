import requests
import allure
from endpoints.endpoint import Endpoint


class CreateObject(Endpoint):

    @allure.step("Отправить POST-запрос на /object")
    def create_new_object(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(f'{self.url}', json=payload, headers=headers)
        self.json = self.response.json()
        return self.response, self.json
