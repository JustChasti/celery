import requests
import json
import time
from api import config


def send(text):
    data = {
        "link": text,
        }
    answer = requests.post('http://127.0.0.1:5000/'+'links/add/',
                           verify=False, data=json.dumps(data),
                           headers=config.headers)
    print(answer)


def test_get():
    answer = requests.get('http://127.0.0.1:5000/' + 'links/all/',
                          verify=False, headers=config.headers).json()
    print(answer)


if __name__ == "__main__":
    test_get()
    # send('https://www.wildberries.ru/catalog/6034394/detail.aspx?targetUrl=XS')
    # send('https://www.ozon.ru/product/izuchaem-python-programmirovanie-igr-vizualizatsiya-dannyh-veb-prilozheniya-metiz-erik-metiz-erik-211432437/')
