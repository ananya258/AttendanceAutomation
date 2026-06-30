from pages.login_page import LoginPage
from pages.logout_page import LogoutPage


def test_logout_session_check(driver):

    driver.get(
        "http://127.0.0.1:5500/website/login.html"
    )

    login = LoginPage(driver)

    login.login(
        "admin",
        "admin123"
    )

    logout = LogoutPage(driver)

    logout.logout()

    driver.back()

    assert "login.html" in driver.current_url