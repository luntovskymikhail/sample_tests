import allure
from utils.pages.base import BasePage

from utils.injector import injector


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        xpath = self.xpath

        self.status_code = xpath("//span[@data-key='response-code']")
        self.response_text = xpath("//pre[@data-key='output-response']")

    @allure.step("Переходит на главную страницу и проверяет содержимое")
    @injector.inject
    def get_main_page(self, text_check):
        self.driver.get(self.base_url)

        check_list = [
            "Test your front-end against a real API",
            "A hosted REST-API ready to respond to your AJAX requests.",
            "SUPPORT REQRES",
            "Check out the Swagger doc:",
        ]

        [self.wait_text(text=i) for i in check_list]

        with allure.step("Проверяет заголовок страницы"):
            text_check(
                expected="Reqres - A hosted REST-API ready to respond to your AJAX requests",
                actual=self.driver.title,
            )

        with allure.step("Проверяет ссылку страницы"):
            text_check(expected=self.base_url, actual=self.driver.current_url)

        return self

    @allure.step("Получает статус код со страницы")
    @injector.inject
    def get_status_code(self, expected_code, text_check):
        page_status_code = self.status_code().text

        with allure.step(f"Ожидаемый статус код {expected_code}"):
            text_check(expected=expected_code, actual=page_status_code)

        return page_status_code

    @allure.step("Получает ответ со страницы")
    def get_response(self):
        return self.response_text().text
