import allure
import pytest

from utils.checks import TextCheck

from utils.pages.MainPage import MainPage

from utils.api.api_users import APIUsers


@allure.epic("UI тесты")
@pytest.mark.ui
class TestMainPage:

    @allure.feature("Сравнивает данные из api запроса с ui")
    # @allure.story("Опциональный третий уровень вложения")
    def test_check_ui_api_code_response(self, driver):
        main_page = MainPage(driver)

        main_page.get_main_page()

        with allure.step("Проверяет соответствие статус кода"):
            TextCheck().check(
                expected=main_page.get_status_code(expected_code="200"),
                actual=APIUsers().get_list_users(page=2)["status_code"]
            )

        with allure.step("Проверяет соответствие ответа"):
            TextCheck().check(
                expected=main_page.get_response(page=2),
                actual=APIUsers().get_list_users()["response"]
            )
