from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# driver = None
#
#
# def setup_module(module):
#     global driver
#     driver = webdriver.Chrome(ChromeDriverManager().install())
#     driver.implicitly_wait(10)
#     driver.delete_all_cookies()
#     driver.get('http://www.google.com')
#
#
# def teardown_module(module):
#     driver.quit()


def test_google():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get('http://www.google.com')
    driver.quit()


def test_facebook():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get('http://www.facebook.com')
    assert driver.title == "Facebook – log in or sign up"
    driver.quit()


def test_insta():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get('http://www.instagram.com')
    assert driver.title == "Instagram"
    driver.quit()


def test_gmail():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get('http://www.gmail.com')
    assert driver.title == "Gmail"
    driver.quit()
