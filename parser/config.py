from os import getenv

headers = {'Content-type': 'application/json', 'Accept': 'text/plain',
           'Content-Encoding': 'utf-8'}
delay = 15
selsleep = 2
selenium_driver_path = "E:\code\celery\parser\chromedriver.exe"
url = getenv('API_URL')
base_user = getenv('POSTGRES_USER')
base_pass = getenv('POSTGRES_PASSWORD')
base_name = getenv('POSTGRES_DB')
base_host = getenv('POSTGRES_HOST')
base_port = getenv('POSTGRES_PORT')
