import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math


@pytest.mark.smoke
def test_guest_should_see_cart_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(5)

    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#add_to_basket_form > button")))
    # WebDriverWait(webdriver.Chrome(), 5).until(EC.element_to_be_clickable((By.ID, "verify")))