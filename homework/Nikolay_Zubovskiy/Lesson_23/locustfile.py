from locust import task, HttpUser
import random


class TestUserTraffic(HttpUser):

    @task(1)
    def get_many_object(self):
        self.client.get(
            '/object'
        )

    @task(3)
    def get_one_object(self):
        self.client.get(
            f'/object/{random.choice([35, 40, 44, 55])}'
        )
