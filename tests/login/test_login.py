from pages.login_page import LoginPage
from testdata.login_data import *


def test_login_success(page):

    login = LoginPage(page)

    login.open()

    login.login(
        VALID_EMAIL,
        VALID_PASSWORD
    )

    assert "/users/login" not in page.url