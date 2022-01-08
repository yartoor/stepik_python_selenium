from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_id("treasure")
    x_value = x.get_attribute("valuex")
    y = calc(x_value)

    answer_input = browser.find_element_by_id("answer")
    answer_input.send_keys(y)

    checkbox_input = browser.find_element_by_id("robotCheckbox")
    checkbox_input.click()

    radiobutton_input = browser.find_element_by_id("robotsRule")
    radiobutton_input.click()

    submit_button = browser.find_element_by_xpath('//form//button[@type="submit"]')
    submit_button.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла