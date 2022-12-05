import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# import unittest
import chromedriver_autoinstaller as chromedriver
chromedriver.install()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import selenium


"""
Ужасно всратое задание, элементы ведут себя нестабильно. ЦСС селектор то находит элемент, то нет. Пришлось 
поштучно проверять каждый. постоянно StaleElementException
"""
@pytest.mark.parametrize('link', [ #"https://stepik.org/lesson/236895/step/1", # Correct
                               #  "https://stepik.org/lesson/236896/step/1", #Correct
                              #   "https://stepik.org/lesson/236897/step/1",
                                  "https://stepik.org/lesson/236898/step/1",  #проверить
                              #   "https://stepik.org/lesson/236899/step/1", #are not
                              #   "https://stepik.org/lesson/236903/step/1",
                              #   "https://stepik.org/lesson/236904/step/1",
                               #  "https://stepik.org/lesson/236905/step/1" #what they seem! OvO
                                  ]
)
def test_registration1(link):
    try:
        # link = "https://stepik.org/lesson/236895/step/1"
        browser = webdriver.Chrome()
        browser.get(link)
        browser.implicitly_wait(5)

        user = "drucewihlis@gmail.com"
        password = "DELETED"

        WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.ID, "ember33")))
        log_in = browser.find_element(By.ID, "ember33")
        log_in.click()
        email_input = browser.find_element(By.ID, "id_login_email")
        email_input.send_keys(user)
        password_input = browser.find_element(By.ID, "id_login_password")
        password_input.send_keys(password)
        log_in_button = browser.find_element(By.CSS_SELECTOR, ".sign-form__btn.button_with-loader")
        log_in_button.click()

        # WebDriverWait(browser, 5).until(
        #     EC.visibility_of_element_located((By.CSS_SELECTOR, ".string-quiz__textarea")))
        time.sleep(5)
        input_textarea = browser.find_element(By.CSS_SELECTOR, ".string-quiz__textarea")
        # time.sleep(5)
        WebDriverWait(browser, 12).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".ember-text-area")))
        # time.sleep(5)

        answer = math.log(int(time.time()))
        input_textarea.send_keys(answer)
        WebDriverWait(browser, 12).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission")))
        # time.sleep(5)
        submit_btn = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
        submit_btn.click()
        # time.sleep(5)
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
        assert browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text == "Correct!", "MY ERROR"


    finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(5)
            # закрываем браузер после всех манипуляций
            browser.quit()