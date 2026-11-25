from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    return chrome_driver


def test_input_field(driver):

    test_text = "autotest_12345"
    driver.get("https://www.qa-practice.com/elements/input/simple")
    input_field = driver.find_element(By.ID, 'id_text_string')
    input_field.send_keys(test_text)
    input_field.send_keys(Keys.ENTER)
    result_element = driver.find_element(By.ID, 'result-text')
    displayed_text = result_element.text
    assert displayed_text == test_text
    print(f"Текст, отображённый на странице: {displayed_text}")
