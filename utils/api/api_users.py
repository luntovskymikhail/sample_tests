import requests
import json
import allure

from utils.api.base import API
from abc import ABC


class UsersError(AssertionError):
    pass


class APIUsers(API, ABC):
    def __init__(self):
        super(APIUsers, self).__init__()

    def _process(self, *args, **kwargs):
        raise DeprecationWarning("Для данного класса нет общего метода _process")

    @allure.step("Получает список пользователей")
    def get_list_users(self, page):
        response = requests.get(
            url=f"{self.api_path}/api/users?page={page}",
            headers={"accept": "application/json"},
        )

        if response.status_code != 200:
            with allure.step(
                f"Провалено с кодом {response.status_code} / Ответ: {response.text}"
            ):
                raise UsersError
        else:
            with allure.step("Успешно с кодом 200"):
                return {
                    "status_code": response.status_code,
                    "response": json.loads(response.text)
                }
