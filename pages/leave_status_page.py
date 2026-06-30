from selenium.webdriver.common.by import By


class LeaveStatusPage:

    leave_status_btn = (By.ID, "leaveStatusBtn")

    leave_status = (By.ID, "leaveStatus")

    def __init__(self, driver):
        self.driver = driver

    def open_leave_status(self):
        self.driver.find_element(
            *self.leave_status_btn
        ).click()

    def get_leave_status(self):
        return self.driver.find_element(
            *self.leave_status
        ).text