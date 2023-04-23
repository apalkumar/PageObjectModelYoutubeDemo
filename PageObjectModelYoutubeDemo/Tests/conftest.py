import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
from Config.config import TestData


# @pytest.fixture(params=["chrome", "firefox"], scope='class')
@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        # web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABEL_PATH)
        # web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver = web_driver
    yield
    web_driver.close()
