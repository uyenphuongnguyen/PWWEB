from pages.base_page import BasePage
from config.config import BASE_URL


class LoginPage(BasePage):

    POPUP = "button[data-key='website-popup']"
    EMAIL = "input[id='email']"

    PASSWORD = "input[id='password']"

    LOGIN = "button[normalize-space()='Login']"

    REMEMBER = "input[name='remember']"

    FORGOT = "a[href*='password/reset']"

    def open(self):
        self.page.goto(BASE_URL + "/users/login")

    def input_email(self, email):
        self.fill(self.EMAIL, email)

    def input_password(self, password):
        self.fill(self.PASSWORD, password)

    def click_login(self):
        self.click(self.LOGIN)

    def login(self, email, password):

        self.input_email(email)

        self.input_password(password)

        self.click_login()

        self.wait()