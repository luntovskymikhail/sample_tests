import requests
import json
import allure

from utils.api.base import API
from utils.injector import injector
from abc import ABC


class RegisterError(AssertionError):
    pass


class APIRegister(API, ABC):
    def _process(self, user_data):
        return requests.post(
            url=f"{self.api_path}/api/register", headers=self.HEADERS, json=user_data
        )

    @allure.step("Регистрирует пользователя")
    def register(self, email, password):
        user_data = {"email": email, "password": password}

        response = self._process(user_data=user_data)

        if response.status_code != 200:
            with allure.step(
                f"Регистрация пользователя провалена с кодом {response.status_code} ответ {response.text}"
            ):
                raise RegisterError
        else:
            with allure.step("Регистрация пользователь успешна с кодом 200"):
                return json.loads(response.text)
