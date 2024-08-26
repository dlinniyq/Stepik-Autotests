import pytest
from selenium import webdriver
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import math

from conftest import browser


@pytest.mark.parametrize("id", ["236895","236896","236897","236898", "236899", "236903", "236904", "236905"])
def test_stepik(browser,id):
    link = f"https://stepik.org/lesson/{id}/step/1"

# def test_stepik(browser):
#     link = f"https://stepik.org/lesson/236898/step/1"
    browser.get(link)

    browser.implicitly_wait(5)

    loggin = browser.find_element(By.CSS_SELECTOR, ".ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button")
    loggin.click()

    e_mail = browser.find_element(By.CSS_SELECTOR, "#id_login_email")
    e_mail.send_keys("nikita.bulgakoff898@gmail.com")

    password = browser.find_element(By.CSS_SELECTOR, "#id_login_password")
    password.send_keys("rebitf98")
    browser.find_element(By.CSS_SELECTOR, ".sign-form__btn.button_with-loader").click()

    time.sleep(5)

    answer_input = browser.find_element(By.CSS_SELECTOR, ".ember-text-area.ember-view.textarea.string-quiz__textarea")
    # answer_input = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".ember-text-area.ember-view.textarea.string-quiz__textarea")))
    answer_num = math.log(int(time.time()))
    answer_input.send_keys((str(answer_num)))

    send_button = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
    send_button.click()
    message = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text
    assert message == "Correct!", message