from selenium import webdriver
import time;
import math;

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    browser.find_element_by_css_selector(".btn").click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    browser.find_element_by_id("answer").send_keys(y)

    browser.find_element_by_tag_name("button").click()

    alert = browser.switch_to.alert
    allertText = alert.text
    print (allertText)
    alert.accept()

finally:
    time.sleep(100)
    browser.quit()
