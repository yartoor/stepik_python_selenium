from selenium import webdriver
import time
import os
try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element_by_name('firstname')
    first_name.send_keys("Антуан")

    last_name = browser.find_element_by_name("lastname")
    last_name.send_keys("Нажарян")

    email = browser.find_element_by_name("email")
    email.send_keys("antuan@gmail.com")
    
    file_input = browser.find_element_by_id('file')
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'lesson2_step6.txt') 
    file_input.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn.btn-primary")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()