from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_id("input_value")
    x_value = int(x.text)
    y = calc(x_value)

    answer_input = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer_input)
    answer_input.send_keys(y)

    checkbox_input = browser.find_element_by_id("robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox_input)
    checkbox_input.click()

    radiobutton_input = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton_input)
    radiobutton_input.click()

    submit_button = browser.find_element_by_xpath('//form//button[@type="submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла