from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Student_Registration_Form as srf


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    return chrome_driver


def test_student_registration_form(driver):
    driver.get("https://demoqa.com/automation-practice-form")
    wait = WebDriverWait(driver, 10)
    driver.find_element(By.ID, "firstName").send_keys(srf["first_name"])
    driver.find_element(By.ID, "lastName").send_keys(srf["last_name"])
    driver.find_element(By.ID, "userEmail").send_keys(srf["email"])
    driver.find_element(By.ID, "userNumber").send_keys(srf["mobile"])
    driver.find_element(By.ID, "currentAddress").send_keys(srf["current_address"])

    subjects_input = driver.find_element(By.ID, "subjectsInput")
    subject = srf["subjects"]
    subjects_input.send_keys(subject)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, f"//div[contains(@class,'subjects-auto-complete__option')"
                   f" and text()='{subject}']")
    )).click()

    gender = srf["gender"]
    driver.find_element(By.XPATH, f"//label[text()='{gender}']").click()

    hobby = srf["hobbies"]
    driver.find_element(By.XPATH, f"//label[text()='{hobby}']").click()

    state = srf["state"]
    driver.find_element(By.ID, "state").click()
    wait.until(EC.element_to_be_clickable((
        By.XPATH, f"//div[@role='option' and text()='{state}']"
    ))).click()

    city = srf["city"]
    wait.until(EC.element_to_be_clickable((By.ID, "city"))).click()
    wait.until(EC.element_to_be_clickable((
        By.XPATH, f"//div[@role='option' and text()='{city}']"
    ))).click()

    dt = datetime.strptime(srf["date_of_birth"], "%d %B %Y")
    day, month, year = str(dt.day), dt.strftime("%B"), str(dt.year)
    date_input = driver.find_element(By.ID, "dateOfBirthInput")
    date_input.click()
    wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".react-datepicker")
    ))
    Select(driver.find_element(By.CSS_SELECTOR, ".react-datepicker__year-select")
           ).select_by_visible_text(year)
    Select(driver.find_element(By.CSS_SELECTOR, ".react-datepicker__month-select")
           ).select_by_visible_text(month)
    driver.find_element(By.XPATH,
                        f"//div[contains(@class,'react-datepicker__day') "
                        f"and not(contains(@class,'--outside-month')) "
                        f"and text()='{day}']").click()

    driver.find_element(By.ID, "submit").click()
    modal = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-content")))
    print("=== Содержимое модального окна ===")
    print(modal.text)
