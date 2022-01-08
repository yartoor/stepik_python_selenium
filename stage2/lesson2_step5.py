from selenium import webdriver
import time 

from selenium.webdriver.support.ui import Select

links = [ 
          "http://suninjuly.github.io/selects1.html",
          "http://suninjuly.github.io/selects2.html"
         ]

for link in links:
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        el_num1 = browser.find_element_by_id("num1")
        el_num2 = browser.find_element_by_id("num2")

        el_num1_value = int(el_num1.text)
        el_num2_value = int(el_num2.text)
        
        select = Select(browser.find_element_by_tag_name("select"))
        select.select_by_value(str(el_num1_value + el_num2_value))

        submit_button = browser.find_element_by_xpath('//form//button[@type="submit"]')
        submit_button.click()
        
    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

# не забываем оставить пустую строку в конце файла