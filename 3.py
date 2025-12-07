from csv import excel
from http.client import responses

import requests

url = input("Введите ссылку: ")

try:
    response = requests.get(url, timeout=5)

    status_code = response.status_code

    if 200 <= status_code < 400:
        print(f"Сайт доступен! Код ответа: {status_code}")
    else:
        print(f"Сайт недоступен! Код ответа: {status_code}")

except requests.exceptions.Timeout:
    print("Ошибка подключения! Таймаут")
except requests.exceptions.ConnectionError:
    print("Ошибка подключения! Нет сети или неправильный адрес.")
except requests.exceptions.RequestException as e:
    print(f"Ошибка подключения! Произошла ошибка при запросе {e}")