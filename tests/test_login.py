import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from utils.config import LOGIN_URL

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get(LOGIN_URL)
    yield driver
    driver.quit()

def test_valid_login(setup):
    login = LoginPage(setup)
    login.login("admin", "admin123")
    assert setup.title == "Dashboard"

def test_invalid_login(setup):
    login = LoginPage(setup)
    login.login("wrong", "wrong")
    assert "Invalid" in setup.page_source
