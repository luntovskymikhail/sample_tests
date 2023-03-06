import allure
import pytest
from utils.api.api_users import APIUsers


@allure.epic("API тесты")
@pytest.mark.api
class TestUsers:

    @allure.feature("Перебирает параметрами пользователей")
    # @allure.story("Опциональный третий уровень вложения")
    @pytest.mark.parametrize("page", [i for i in range(1, 4)])
    def test_register(self, page):
        APIUsers().get_list_users(page=page)