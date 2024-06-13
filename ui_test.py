import requests
import json
import pytest
import allure

def test_podobrat_tour():
    driver = webdriver.Chrome() #Открываем браузер
    Main = Main(driver)
    Main.podobrat_tour()
    assert result_page() == '#class="tour-order"'
  
    driver.quit()