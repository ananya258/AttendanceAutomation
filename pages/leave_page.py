from selenium.webdriver.common.by import By


class LeavePage:

    leave_btn = (By.ID, "leaveBtn")

    leave_type = (By.ID, "leaveType")
    start_date = (By.ID, "startDate")
    end_date = (By.ID, "endDate")
    reason = (By.ID, "reason")

    submit_btn = (By.XPATH, "//button[contains(text(),'Submit')]")

    leave_message = (By.ID, "leaveMessage")

    def __init__(self, driver):
        self.driver = driver

    def open_leave_page(self):
        self.driver.find_element(*self.leave_btn).click()

    def apply_leave(self):

        self.driver.find_element(*self.start_date).send_keys(
            "2026-06-18"
        )

        self.driver.find_element(*self.end_date).send_keys(
            "2026-06-29"
        )

        self.driver.find_element(*self.reason).send_keys(
            "fever"
        )

        self.driver.find_element(*self.submit_btn).click()

    def apply_leave_invalid(self):

        self.driver.find_element(
            *self.submit_btn
        ).click()

    def get_message(self):
        return self.driver.find_element(
            *self.leave_message
        ).text