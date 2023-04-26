import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = None


@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("-----------------Setup-------------------")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get('http://www.google.com')
    yield
    print("-----------------teardown-------------------")
    driver.quit()


# def teardown_module(module):
#     print("-----------------teardown-------------------")
#     driver.quit()

@pytest.mark.usefixtures("init_driver")
# def test_google_title(init_driver):
def test_google_title():
    assert driver.title == "Google", "Failed"


@pytest.mark.usefixtures("init_driver")
# def test_google_url(init_driver):
def test_google_url():
    assert driver.current_url == "https://www.google.com/"
