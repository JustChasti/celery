from os import getenv
"""     Настройки:
            headers - заголовки
            url - сервер flask
            base name pass user - настройки подключения к postgres
            delay - задержка парсинга (для теста - 60 секунд, для работы 3600)
        Инструкция:
            1) запустить app (flask)
            2) запустить parser
            3) можно запустить тесты
"""


headers = {'Content-type': 'application/json', 'Accept': 'text/plain',
           'Content-Encoding': 'utf-8'}
delay = 60
url = 'http://127.0.0.1:5000/'
base_user = getenv('POSTGRES_USER')
base_pass = getenv('POSTGRES_PASSWORD')
base_name = getenv('POSTGRES_DB')
base_host = getenv('POSTGRES_HOST')
base_port = getenv('POSTGRES_PORT')
