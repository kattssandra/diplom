import requests
import json
from MainApi import Tourist
import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

url = "https://auth2.fstravel.com/api/v1/account/sign-up-buyer"


#1 Проверим, что в заголовке объекта resp передается контент в формате JSON с кодировкой UTF-8:

def test_simple_req():
    resp = requests.get('https://auth2.fstravel.com/api/v1/account/sign-up-buyer')
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json; charset=utf-8"

# регистрация с почтой в домене .ru:
def test_add_new_ru():
    resp = requests.get('https://auth2.fstravel.com/api/v1/account/sign-up-buyer')
    Tourist.create_ru(self, test@skypro.ru, QA78, +7985899998787)
    assert resp.status_code == 200
    