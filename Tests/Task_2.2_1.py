from selenium import webdriver
import time
import math

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    
    sum = int(num1)+ int(num2)
    print (sum)
    
    dropdown= browser.find_element_by_id("dropdown")
    dropdown.click()
    attribute = "//option[@value='"+str(sum)+"']"
    browser.find_element_by_xpath(attribute).click()

    browser.find_element_by_class_name("btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
