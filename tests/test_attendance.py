from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def login_to_dashboard(driver):

    driver.get(
        "http://127.0.0.1:5500/website/login.html"
    )

    login = LoginPage(driver)

    login.login(
        "admin",
        "admin123"
    )


def test_mark_attendance(driver):

    login_to_dashboard(driver)

    dashboard = DashboardPage(driver)

    dashboard.mark_attendance()

    assert (
        dashboard.get_attendance_message()
        ==
        "Attendance marked successfully"
    )


def test_duplicate_attendance(driver):

    login_to_dashboard(driver)

    dashboard = DashboardPage(driver)

    dashboard.mark_attendance()

    dashboard.mark_attendance()

    assert (
        dashboard.get_attendance_message()
        ==
        "Attendance already marked"
    )