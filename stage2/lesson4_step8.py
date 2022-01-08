from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time 
import math


link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_id("book")

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),'100')
    )
    button.click()
    
    x_el = browser.find_element_by_id('input_value')
    x_value = x_el.text
    y = calc(x_value)

    answer_input = browser.find_element_by_id("answer")
    answer_input.send_keys(y)

    submit_button = browser.find_element_by_xpath('//form//button[@id="solve"]')
    submit_button.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла