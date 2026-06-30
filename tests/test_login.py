from pages.login_page import LoginPage
from selenium.webdriver.common.by import By


def test_valid_login(driver):

    driver.get("http://127.0.0.1:5500/website/login.html")

    login = LoginPage(driver)
    login.login("admin", "admin123")

    assert "dashboard" in driver.current_url.lower()


def test_invalid_login(driver):

    driver.get("http://127.0.0.1:5500/website/login.html")

    login = LoginPage(driver)
    login.login("admin", "wrong123")

    message = driver.find_element(By.ID, "message").text

    assert message == "Invalid Credentials"


def test_empty_login(driver):

    driver.get("http://127.0.0.1:5500/website/login.html")

    login = LoginPage(driver)
    login.login("", "")

    message = driver.find_element(By.ID, "message").text

    assert message == "Fields cannot be empty"