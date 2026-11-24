import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    return chrome_driver


def test_single_select(driver):
    driver.get("https://www.qa-practice.com/elements/select/single_select")
    wait = WebDriverWait(driver, 10)

    language = "JavaScript"
    select_element = driver.find_element(By.ID, "id_choose_language")
    Select(select_element).select_by_visible_text(language)

    driver.find_element(By.NAME, "submit").click()

    result = wait.until(EC.visibility_of_element_located((By.ID, "result-text")))

    assert language in result.text
