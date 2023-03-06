import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    d = webdriver.Chrome(ChromeDriverManager().install())
    d.set_window_size(1920, 1080)
    d.implicitly_wait(10)
    d.set_page_load_timeout(30)
    yield d
    d.quit()
