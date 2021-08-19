from config import selenium_driver_path
from selenium import webdriver


def download(link):
    driver = webdriver.Chrome(executable_path=selenium_driver_path)
    driver.get(link)
    html = driver.page_source
    return html


if __name__ == "__main__":
    download('https://www.ozon.ru/product/tabletki-dlya-posudomoechnyh-mashin-synergetic-besfosfatnye-55-sht-55-sht-181952391/reviews/')
