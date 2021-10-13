from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:

    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    browser.find_element_by_id("answer").send_keys(y)

    browser.find_element_by_id("robotCheckbox").click()

    button = browser.find_element_by_tag_name("button")

    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element_by_id("robotsRule").click()
    button.click()

finally:
    time.sleep(10)
    browser.quit()
