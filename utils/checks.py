import allure
from abc import ABC, abstractmethod


class CheckDateError(AssertionError):
    pass


class CheckSummError(AssertionError):
    pass


class CheckTextError(AssertionError):
    pass


class BaseCheck(ABC):
    @abstractmethod
    def check(self, *args, **kwargs):
        pass


class DateCheck(BaseCheck):
    """Проверка даты"""

    def check(self, expected, actual):
        with allure.step(f"Ожидаемая дата: {expected}"):
            pass

        with allure.step(f"Фактическая дата: {actual}"):
            if actual != expected:
                raise CheckDateError
            else:
                with allure.step("Ожидаемая дата совпадает с фактической"):
                    return None


class SummCheck(BaseCheck):
    """Проверка суммы"""

    def check(self, expected, actual):
        with allure.step(f"Ожидаемая сумма: {expected}"):
            pass

        if expected != actual:
            with allure.step(f"Получена не правильная сумма: {actual}"):
                raise CheckSummError
        else:
            with allure.step("Ожидаемая сумма совпадает с фактической"):
                return None


class TextCheck(BaseCheck):
    """Проверка текста"""

    def check(self, expected, actual):
        with allure.step(f"Ожидаемый текст: {expected}"):
            pass

        if expected != actual:
            with allure.step(f"Получен неправильный текст: {actual}"):
                raise CheckTextError
        else:
            with allure.step("Ожидаемый текст совпадает с фактическим"):
                return None
