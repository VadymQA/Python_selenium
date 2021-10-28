import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math

# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()

@pytest.mark.parametrize('pages', ["236895", "236896","233897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, pages):

    link = f"https://stepik.org/lesson/{pages}/step/1"
    browser.get(link)
    time.sleep(5)

    browser.find_element_by_css_selector(".ember-text-area").send_keys(str(math.log(int(time.time()))))
    browser.find_element_by_class_name("submit-submission").click()
    time.sleep(5)

    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CLASS_NAME,"smart-hints__hint")))
    WebDriverWait(browser, 5).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "smart-hints__hint"), "Correct!"))
    msg = browser.find_element_by_class_name("smart-hints__hint").text

    if ((msg == "Correct!") == False):
        print(msg)

    assert msg == "Correct!"


