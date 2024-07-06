import allure
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ActionChains

MAIN_URL = "https://fstravel.com/"

class MainPage:
      def __init__(self, driver):
        self._driver = driver
        self._driver.get(MAIN_URL)
        self.actions = ActionChains(driver)  # Двоной клик
        self.wait = WebDriverWait(driver, 12)  # Ожидание 10 сек

      with allure.step("Работоспособность кнопки Подобрать тур"):
          def podobrat_tour(self,term):
               self._driver.find_element(By.XPATH, "//*[@id="app"]/div/header/div[1]/div/div/div/div[1]/div[2]/a[1]").click()
               
      with allure.step("Работоспособность кнопки “Отзыв на сайте"):
          def otzyv(self,term):
               self._driver.find_element(By.XPATH, "//*[@id="uxs_cepveveb27f1by13h327kin5"]/img").click()
      
      with allure.step("Работоспособность кнопки “Горящие туры"):
          def gor_toury(self,term):
               self._driver.find_element(By.XPATH, "///*[@id="app"]/div/header/div[2]/div/nav/a[7]").click()

      with allure.step("Работоспособность кнопки Профиля"):
          def profile(self,term):
               self._driver.find_element(By.XPATH, "//*[@id="app"]/div/header/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[1]/img").click()
      
      with allure.step("Закрытие веб-браузера"):
            def close_driver(self):
                self._driver.quit()