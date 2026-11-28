import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
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


def test_add_to_cart_via_hover(driver):
    driver.get("http://testshop.qa-practice.com/")
    wait = WebDriverWait(driver, 10)

    product_img = driver.find_elements(By.CSS_SELECTOR, "img[itemprop='image']")[0]
    product_name = driver.find_elements(By.CSS_SELECTOR, "a[itemprop='name']")[0]
    product_text = product_name.text

    ActionChains(driver).move_to_element(product_img).perform()

    cart_btn = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a[title='Shopping cart']")
        )
    )
    cart_btn.click()

    popup = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".modal-content")
        )
    )
    assert product_text in popup.text, \
        f"Товар '{product_text}' не найден в попапе. Текст попапа: {popup.text.lower()}"
