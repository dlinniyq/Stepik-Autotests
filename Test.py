from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import *
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price" ), "$100" ))
    browser.find_element(By.CSS_SELECTOR, "#book").click()

    x_text = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_text.text
    y = log(abs(12*sin(int(x))))
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "#solve").click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(8)
    # закрываем браузер после всех манипуляций
    browser.quit()