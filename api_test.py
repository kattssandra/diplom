import requests
import json
import pytest
import allure
from faker import Faker

url = "https://auth2.fstravel.com/api/v1/account/sign-up-buyer"

#1 Проверим, что в заголовке объекта resp передается контент в формате JSON с кодировкой UTF-8:

def simple_req_test():
    resp = requests.get(url)
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json; charset=utf-8"

# 2 регистрация с почтой в домене .ru:
def test_ru():
        reg_params = {
        "email" : '1wc@mail.ru',
        "password": '%2B21%40.ru',
        "phoneNumber" : '+79874561232',
        "emailing" : 'true',
        "clientId" : 'b2c:ru',
        "grant_type" : 'client_credentials',
        "clientType" : 'b2c.public.client'
    }
        response = requests.post(url, params=reg_params)
        assert response.status_code == 201
    
# 3 регистрация с почтой в домене .com:
def test_com():
        reg_params3 = {
        "email" : '17vfg3@gmail.com',
        "password": '%2B21%40456',
        "phoneNumber" : '+79874578232',
        "emailing" : 'true',
        "clientId" : 'b2c:ru',
        "grant_type" : 'client_credentials',
        "clientType" : 'b2c.public.client'
    }
        response2 = requests.post(url, params=reg_params3)
        assert response2.status_code == 201

# 4 регистрация только с обязательными полями
def test_field():
        reg_params4 = {
        "email" : '1v5s3@gmail.com',
        "password": '1505198556',
        "phoneNumber" : '+74958636875',
        "emailing" : 'true',
        "clientId" : 'b2c:ru',
        "grant_type" : 'client_credentials',
        "clientType" : 'b2c.public.client'
    }
        response3 = requests.post(url, params=reg_params4)
        assert response3.status_code == 201

# 5 Регистрация с максимальным количеством символов в пароле
def test_max():
        reg_params5 = {
        "email" : '1175vs3@gmail.com',
        "password": '1234697897',
        "phoneNumber" : '+7496963689',
        "emailing" : 'true',
        "clientId" : 'b2c:ru',
        "grant_type" : 'client_credentials',
        "clientType" : 'b2c.public.client'
    }
        response3 = requests.post(url, params=reg_params5)
        assert response3.status_code == 201
