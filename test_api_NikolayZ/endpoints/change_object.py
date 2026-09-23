import requests
import allure
from endpoints.endpoint import Endpoint


class ChangeObject(Endpoint):
    @allure.step("Отправить PATCH-запрос на обновление объекта /object/{object_id} с новыми данными")
    def update_object(self, object_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f'{self.url}/{object_id}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response, self.json
