from selenium.webdriver.common.by import By


class DashboardPage:

    attendance_btn = (By.ID, "attendanceBtn")
    attendance_msg = (By.ID, "attendanceMessage")

    def __init__(self, driver):
        self.driver = driver

    def mark_attendance(self):
        self.driver.find_element(
            *self.attendance_btn
        ).click()

    def get_attendance_message(self):
        return self.driver.find_element(
            *self.attendance_msg
        ).text