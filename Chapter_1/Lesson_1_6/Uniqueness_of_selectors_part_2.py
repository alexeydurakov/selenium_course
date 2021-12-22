from selenium import webdriver
import time

from selenium.webdriver.common.by import By

try:
    #link = "http://suninjuly.github.io/registration1.html"
    link= "http://suninjuly.github.io/registration2.html"

    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input_first = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
    input_first.send_keys("Ivan")

    input_last = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
    input_last.send_keys("Ivanov")

    input_last = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
    input_last.send_keys("Ivan@ivanov.ru")


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


    #Результат

    #selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element:
    # {"method":"xpath","selector":"//input[@placeholder='Input your first name']"}