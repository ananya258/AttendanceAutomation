from pages.login_page import LoginPage
from pages.leave_page import LeavePage


def login_to_dashboard(driver):

    driver.get(
        "http://127.0.0.1:5500/website/login.html"
    )

    login = LoginPage(driver)

    login.login(
        "admin",
        "admin123"
    )


def test_apply_leave(driver):

    login_to_dashboard(driver)

    leave = LeavePage(driver)

    leave.open_leave_page()

    leave.apply_leave()

    assert (
        leave.get_message()
        ==
        "Leave Request Submitted | Status: Pending"
    )


def test_leave_validation(driver):

    login_to_dashboard(driver)

    leave = LeavePage(driver)

    leave.open_leave_page()

    leave.apply_leave_invalid()

    assert (
        leave.get_message()
        ==
        "All fields are mandatory"
    )