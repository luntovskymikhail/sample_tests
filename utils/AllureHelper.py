import allure
from allure_commons.types import AttachmentType


class AllureHelper:
    def __init__(self, driver):
        self.driver = driver

    def screenshot(self):
        """
        Сделает скриншот и ничего больше.
        """
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="screenshot_failed_test",
            attachment_type=AttachmentType.PNG,
        )
