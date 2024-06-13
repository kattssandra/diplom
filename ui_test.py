import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from MainUI import MainPage

@allure.title("Кнопка Подобрать тур")
@allure.description("Тест проверяет работоспособность кнопки")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.positive_test

def test_podobrat_tour():
    driver = webdriver.Chrome() 
    MainPage.podobrat_tour()
    
@allure.title("Кнопка Отзыв на сайте")
@allure.description("Работоспособность кнопки “Отзыв на сайте")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.positive_test

def test_podobrat_tour():
    driver = webdriver.Chrome() 
    MainPage.otzyv()

@allure.title("Кнопка Горящие туры")
@allure.description("Работоспособность кнопки “Горящие туры")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.positive_test

def test_podobrat_tour():
    driver = webdriver.Chrome() 
    MainPage.gor_toury()

@allure.title("Кнопка Профиля")
@allure.description("Работоспособность кнопки Профиля")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.positive_test

def test_podobrat_tour():
    driver = webdriver.Chrome() 
    MainPage.profile()

    driver.quit()