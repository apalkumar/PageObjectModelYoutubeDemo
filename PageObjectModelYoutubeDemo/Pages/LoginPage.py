from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.HomePage import HomePage


class LoginPage(BasePage):
    # EMAIL = (By.ID, "username")
    # PASSWORD = (By.ID, "password")
    # LOGIN_BUTTON = (By.ID, "loginBtn")
    # SIGNUP_LINK = (By.LINK_TEXT, "Sign up")

    UserName = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    # LOGIN_BUTTON = (By.ID, "loginBtn")
    SIGNUP_LINK = (By.XPATH, "//button[@type='submit']")

    """Constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """ Page Action"""

    """this is used to get the page title"""

    def login_page_title(self, title):
        return self.get_title(title)

    """this is used to get the sign up lnk"""

    def is_signup_link_exist(self):
        return self.is_visible(self.SIGNUP_LINK)

    """this is used to login to app"""

    def do_login(self, username, password):
        self.do_send_keys(self.UserName, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.SIGNUP_LINK)
        return HomePage(self.driver)

