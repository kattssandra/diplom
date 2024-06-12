from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

class Main:
    
    def __init__(self, driver): 
        self._driver = driver
        self._driver.get("https://fstravel.com/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()
               
        # Нажми кнопку Подобрать тур
    def podobrat_tour(self):
        self._driver.find_element(By.CSS_SELECTOR, 'class="v-expert v-header-left-link trslt"').click()
             
    def result_page(self):        
        waiter = WebDriverWait(self.driver, 60)
        waiter.until(EC.text_to_be_present_in_element(By.CSS_SELECTOR, 'class="tour-order"'))
        

