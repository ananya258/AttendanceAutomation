from pages.login_page import LoginPage
from pages.leave_page import LeavePage
from pages.leave_status_page import LeaveStatusPage


def login_to_dashboard(driver):

    driver.get(
        "http://127.0.0.1:5500/website/login.html"
    )

    login = LoginPage(driver)

    login.login(
        "admin",
        "admin123"
    )


def test_view_leave_status(driver):

    login_to_dashboard(driver)

    leave = LeavePage(driver)

    leave.open_leave_page()

    leave.apply_leave()

    status_page = LeaveStatusPage(driver)

    driver.back()

    status_page.open_leave_status()

    status_text = status_page.get_leave_status()

    assert "Sick Leave" in status_text

    assert "Pending" in status_text