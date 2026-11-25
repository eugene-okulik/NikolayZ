import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    return chrome_driver


def test_dynamic_loading(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    wait = WebDriverWait(driver, 15)

    driver.find_element(By.XPATH, "//div[@id='start']/button").click()

    finish = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//div[@id='finish']"))
    )
    assert finish.text == "Hello World!"
