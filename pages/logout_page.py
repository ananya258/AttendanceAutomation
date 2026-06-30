from selenium.webdriver.common.by import By


class LogoutPage:

    logout_btn = (By.ID, "logoutBtn")

    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        self.driver.find_element(
            *self.logout_btn
        ).click()