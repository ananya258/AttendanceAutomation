from selenium.webdriver.common.by import By

class LoginPage:

    username = (By.ID, "username")
    password = (By.ID, "password")
    login_btn = (By.ID, "loginBtn")

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, user):
        self.driver.find_element(*self.username).send_keys(user)

    def enter_password(self, pwd):
        self.driver.find_element(*self.password).send_keys(pwd)

    def click_login(self):
        self.driver.find_element(*self.login_btn).click()

    def login(self, user, pwd):
        self.enter_username(user)
        self.enter_password(pwd)
        self.click_login()