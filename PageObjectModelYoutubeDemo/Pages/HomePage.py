from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage


class HomePage(BasePage):
    HEADER = (By.CSS_SELECTOR, "span.oxd-topbar-header-breadcrumb")

    def __init__(self, driver):
        super().__init__(driver)

    def is_header_exist(self):
        return self.is_visible(self.HEADER)

