from selenium.webdriver.common.by import By

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver

    user = (By.ID, "reg_username")
    pwd = (By.ID, "reg_password")
    btn = (By.ID, "registerBtn")

    def register(self, u, p):
        self.driver.find_element(*self.user).send_keys(u)
        self.driver.find_element(*self.pwd).send_keys(p)
        self.driver.find_element(*self.btn).click()
