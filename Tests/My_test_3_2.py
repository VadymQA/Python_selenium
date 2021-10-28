import time
import unittest
from selenium import webdriver

class TestAssertEqual(unittest.TestCase):
    def test_asser1(self):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)
            input = browser.find_element_by_css_selector(".first_block>.form-group.first_class >.form-control")
            input.send_keys("TestFirst")
            input = browser.find_element_by_css_selector(
                "div.first_block>.form-group.second_class> .form-control.second")
            input.send_keys("TestSecond")
            input = browser.find_element_by_css_selector(".form-control.third")
            input.send_keys("test@test.com")
            button = browser.find_element_by_css_selector("button.btn")
            button.click()
            time.sleep(1)
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            welcome_text = welcome_text_elt.text
            assert "Congratulations! You have successfully registered!" == welcome_text

        finally:
            time.sleep(10)
            browser.quit()
            # self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "test msg")

    def test_asser2(self):
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)
            input = browser.find_element_by_css_selector(".first_block>.form-group.first_class >.form-control")
            input.send_keys("TestFirst")
            input = browser.find_element_by_css_selector(
                "div.first_block>.form-group.second_class> .form-control.second")
            input.send_keys("TestSecond")
            input = browser.find_element_by_css_selector(".form-control.third")
            input.send_keys("test@test.com")
            button = browser.find_element_by_css_selector("button.btn")
            button.click()
            time.sleep(1)
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            welcome_text = welcome_text_elt.text
            assert "Congratulations! You have successfully registered!" == welcome_text
        finally:
            time.sleep(10)
            browser.quit()
            # //self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "test msg")

if __name__ == "__main__":
    unittest.main()

    print("Everything passed")
