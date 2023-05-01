import pytest

from Config.config import TestData
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_Login(BaseTest):
    def test_header_visible(self):
        self.loginPage = LoginPage(self.driver)
        self.homepage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.homePage = HomePage(self.driver)
        flag = self.homePage.is_header_exist()
        assert flag
