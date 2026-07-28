from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    return driver


def test_button_exist(driver):
    driver.get("https://www.qa-practice.com/elements/button/simple")
    assert driver.find_element(By.ID, "submit-id-submit").is_displayed()

def hello(driver):
    driver.get("https://www.qa-practice.com/elements/button/simple")
    assert driver.find_element(By.ID, "submit-id-submit").is_displayed()