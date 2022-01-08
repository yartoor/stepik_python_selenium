from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # ��� ���, ������� ��������� ������������ ����
    element1 = browser.find_element_by_css_selector('.first_block .first')
    element1.send_keys("��� �����")
    element1 = browser.find_element_by_css_selector('.first_block .second')
    element1.send_keys("��� �����")
    element1 = browser.find_element_by_css_selector('.first_block .third')
    element1.send_keys("��� �����")
    # ���������� ����������� �����
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    # ���������, ��� ������ ������������������
    # ���� �������� ��������
    time.sleep(1)
    # ������� �������, ���������� �����
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # ���������� � ���������� welcome_text ����� �� �������� welcome_text_elt
    welcome_text = welcome_text_elt.text
    # � ������� assert ���������, ��� ��������� ����� ��������� � ������� �� �������� �����
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
# �������� ����� ��������� ������� ���������� ����������� �������
    time.sleep(10)
    # ��������� ������� ����� ���� �����������
    browser.quit()
