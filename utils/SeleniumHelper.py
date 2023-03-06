import allure
from utils.AllureHelper import AllureHelper
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class SeleniumHelper:
    """
    Класс для упрощенной работы с селениумом.
    """

    def __init__(self, driver):
        self.driver = driver
        self.screenshot = AllureHelper(driver).screenshot

    def scroll(self, height="to_middle"):
        """
        Скроллит страницу на определенную высоту.

        :param height: to_top, to_middle, to_end или значение int в пикселях
        """

        size = self.driver.get_window_size()["width"]
        scroll = self.driver.execute_script

        error_text = (
            "в метод scroll_down передан не правильный агрумент, "
            "скорее всего опечатка, текстом я принимаю только "
            '"to_middle" и "to_end"'
        )

        try:
            if height == "to_top":
                scroll("window.scrollTo(0, 0)")
            elif height == "to_middle":
                scroll(f"window.scrollTo(0, {int(size) / 2})")
            elif height == "to_end":
                scroll("window.scrollTo(0, document.body.scrollHeight);")
            elif isinstance(size, int):
                scroll(f"window.scrollTo(0, {int(height)})")
        except ValueError:
            raise ValueError(error_text)

    def wait_hide(self, element, seconds: int = 10):
        """
        Явное ожидание, ждет пока элемент не пропадет с экрана

        :param element: какой элемент ждем
        :param seconds: сколько ждем (по умолчанию 10 секунд)
        """

        error_text = (
            f"Ждал пока элемент пропадет с экрана на протяжении "
            f"{seconds} секунд, смотри скришнот во вложении "
        )

        try:
            WebDriverWait(self.driver, seconds).until(
                EC.invisibility_of_element_located(element)
            )
        except TimeoutException:
            with allure.step(f"{error_text}"):
                self.screenshot()
                raise AssertionError(error_text)

    def wait_appear(self, element, seconds: int = 10):
        """
        Явное ожидание, ждет пока элемент появится на экране

        :param element: какой элемент ждем
        :param seconds: сколько ждем (по умолчанию 10 секунд)
        """

        error_text = (
            f"Ждал пока элемент появится на экране на протяжении "
            f"{seconds} секунд, смотри скришнот во вложении "
        )

        try:
            WebDriverWait(self.driver, seconds).until(EC.visibility_of(element))
        except TimeoutException:
            with allure.step(f"{error_text}"):
                self.screenshot()
                raise AssertionError(error_text)

    def switch_window(self, window: int):
        """
        Переключается на определенную вкладку в случае если открыто несколько.

        :param window: целое число, номер вкладки.
        """
        self.driver.switch_to.window(self.driver.window_handles[window])

    def hover_on(self, element):
        """
        Имитирует наведение курсора на элемент.

        :param element: элемент на который необходимо навести курсор.
        """
        with allure.step(f"Навожу курсор на {element}"):
            ActionChains(self.driver).move_to_element(element).perform()

    def wait_text(self, text: str, by="xpath", locator="//body", seconds: int = 10):
        """
        Явное ожидание, ждет пока текст появится на экране

        :param by: метод поиска текста
        :param locator: собственно локатор
        :param text: какой текст ждем
        :param seconds: сколько ждем (по умолчанию 10 секунд)
        """

        error_text = (
            f'Ждал пока появится текст: "{text}" на протяжении {seconds} '
            f"секунд, смотри скриншот во вложении."
        )

        if by == "cls_name":
            method = By.CLASS_NAME
        elif by == "name":
            method = By.NAME
        elif by == "css":
            method = By.CSS_SELECTOR
        elif by == "xpath":
            method = By.XPATH
        elif by == "find_id":
            method = By.ID
        else:
            raise TypeError(f"Не знаю такого метода By.{by}")

        try:
            WebDriverWait(self.driver, seconds).until(
                EC.text_to_be_present_in_element((method, locator), text)
            )
        except TimeoutException:
            with allure.step(f"{error_text}"):
                self.screenshot()
                raise AssertionError(error_text)

    def wait_clickable(self, element, seconds: int = 10):
        """
        Явное ожидание, ждет пока по элементу можно будет кликнуть

        :param element: какой элемент ждем
        :param seconds: сколько ждем (по умолчанию 10 секунд)
        """

        error_text = (
            f"Ждал пока элемент будет кликабелен {seconds} секунд, "
            f"смотри скришнот во вложении "
        )

        try:
            WebDriverWait(self.driver, seconds).until(
                EC.element_to_be_clickable(element)
            )
        except TimeoutException:
            with allure.step(f"{error_text}"):
                self.screenshot()
                raise AssertionError(error_text)
