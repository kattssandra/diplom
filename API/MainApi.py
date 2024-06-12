import requests

class Tourist:
    # Инициализация 
    def __init__(self, url) -> None:
        self.url = url
    # регистрация с почтой в домене .ru:
    def create_ru(self, email, password, phoneNumber):
        tourist = {
            "email": email,
            "password": password,
            "phoneNumber": phoneNumber,
                    }
        my_headers = {}
        resp = requests.post(self.url,json=tourist, headers=my_headers)
        return resp.json()