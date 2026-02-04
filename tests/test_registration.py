from selenium import webdriver
from pages.registration_page import RegistrationPage
from utils.config import REGISTER_URL

def test_registration():
    driver = webdriver.Chrome()
    driver.get(REGISTER_URL)
    reg = RegistrationPage(driver)
    reg.register("vivek", "12345")
    assert "Success" in driver.page_source
    driver.quit()
