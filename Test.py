import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
link_1 = "http://suninjuly.github.io/registration1.html"
link_2 = "http://suninjuly.github.io/registration2.html"

class TestAbs(unittest.TestCase):

    def test_1(self):
        browser.get(link_1)
        first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
        first_name.send_keys("Nikita")

        last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
        last_name.send_keys("Bulgakov")

        email = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
        email.send_keys("123@ya.ru")

        browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Ошибка в тесте №1")

    def test_2(self):
        browser.get(link_2)
        first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
        first_name.send_keys("Nikita")

        last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
        last_name.send_keys("Bulgakov")

        email = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
        email.send_keys("123@ya.ru")

        browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Ошибка в тесте №2")

if __name__ == "__main__":
    unittest.main()