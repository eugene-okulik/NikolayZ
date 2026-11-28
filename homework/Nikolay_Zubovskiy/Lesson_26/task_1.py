import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--unsafely-treat-insecure-origin-as-secure=http://testshop.qa-practice.com")
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.maximize_window()
    return chrome_driver


def test_add_to_cart_via_new_tab(driver):
    driver.get("http://testshop.qa-practice.com/")
    wait = WebDriverWait(driver, 10)
    product_name = driver.find_elements(By.CSS_SELECTOR, "a[itemprop='name']")[0]
    product_text = product_name.text
    ActionChains(driver).key_down(Keys.COMMAND).click(product_name).key_up(Keys.COMMAND).perform()

    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    driver.find_element(By.ID, "add_to_cart").click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-secondary"))).click()
    wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".my_cart_quantity"),
            "1"))

    driver.close()
    driver.switch_to.window(tabs[0])

    driver.find_element(By.CSS_SELECTOR, "a[aria-label='eCommerce cart']").click()
    text = driver.find_element(By.TAG_NAME, "h6").text
    assert product_text in text, f"Товар '{product_text}' не найден в корзине. В корзине {text}"
