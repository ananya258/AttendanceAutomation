from selenium.webdriver.common.by import By


class AdminPage:

    admin_btn = (By.ID, "adminBtn")

    approve_btn = (By.ID, "approveBtn")

    admin_message = (By.ID, "adminMessage")

    def __init__(self, driver):
        self.driver = driver

    def open_admin_page(self):
        self.driver.find_element(
            *self.admin_btn
        ).click()

    def approve_leave(self):
        self.driver.find_element(
            *self.approve_btn
        ).click()

    def get_message(self):
        return self.driver.find_element(
            *self.admin_message
        ).text