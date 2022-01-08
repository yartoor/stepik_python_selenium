from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    alert_button = browser.find_element_by_xpath('//form//button[@type="submit"]')
    alert_button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    x_el = browser.find_element_by_id('input_value')
    x_value = x_el.text
    y = calc(x_value)

    answer_input = browser.find_element_by_id("answer")
    answer_input.send_keys(y)

    submit_button = browser.find_element_by_xpath('//form//button[@type="submit"]')
    submit_button.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла