from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.firefox.options import Options



@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    return driver


def test_button_exist(driver):
    driver.get("https://www.qa-practice.com/elements/button/simple")
    assert driver.find_element(By.ID, "submit-id-submit").is_displayed()


def test_button_exist_2(driver):
    driver.get("https://www.qa-practice.com/elements/button/like_a_button")
    assert driver.find_element(By.PARTIAL_LINK_TEXT, 'Click')
