from selenium.webdriver.common.by import By


class LocatorHelper:
    def __init__(self, driver):
        self.driver = driver

    def _find_element(self, method, path, many=False):
        if not many:
            return lambda: self.driver.find_element(method, path)
        else:
            return lambda: self.driver.find_elements(method, path)

    def css(self, *args, **kwargs):
        return self._find_element(By.CSS_SELECTOR, *args, **kwargs)

    def xpath(self, *args, **kwargs):
        return self._find_element(By.XPATH, *args, **kwargs)

    def find_id(self, *args, **kwargs):
        return self._find_element(By.ID, *args, **kwargs)

    def name(self, *args, **kwargs):
        return self._find_element(By.NAME, *args, **kwargs)

    def tag(self, *args, **kwargs):
        return self._find_element(By.TAG_NAME, *args, **kwargs)

    def class_name(self, *args, **kwargs):
        return self._find_element(By.CLASS_NAME, *args, **kwargs)

    def link(self, *args, **kwargs):
        return self._find_element(By.LINK_TEXT, *args, **kwargs)
