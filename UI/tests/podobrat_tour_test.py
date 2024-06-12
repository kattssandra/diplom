from UI.Main import Main
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_podobrat_tour():
    driver = webdriver.Chrome() #Открываем браузер
    Main = Main(driver)
    Main.podobrat_tour()
    assert result_page() == '#class="tour-order"'
  
    driver.quit()