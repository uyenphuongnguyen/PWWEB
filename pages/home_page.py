from pages.base_page import BasePage


class HomePage(BasePage):

    ACCOUNT = "text=My Account"

    LOGOUT = "text=Logout"

    def verify_login_success(self):

        assert "dashboard" not in self.page.url

        assert "login" not in self.page.url