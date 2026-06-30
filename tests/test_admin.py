from pages.login_page import LoginPage
from pages.leave_page import LeavePage
from pages.admin_page import AdminPage


def login_to_dashboard(driver):

    driver.get(
        "http://127.0.0.1:5500/website/login.html"
    )

    login = LoginPage(driver)

    login.login(
        "admin",
        "admin123"
    )


def test_admin_approval(driver):

    login_to_dashboard(driver)

    leave = LeavePage(driver)

    leave.open_leave_page()

    leave.apply_leave()

    driver.back()

    admin = AdminPage(driver)

    admin.open_admin_page()

    admin.approve_leave()

    assert (
        admin.get_message()
        ==
        "Leave Approved Successfully"
    )