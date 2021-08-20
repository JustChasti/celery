from time import sleep
import os

from loguru import logger

from config import selenium_driver_path, selsleep
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


SELENIUM_GRID_HOST = os.environ.get('SELENIUM_GRID_HOST', 'selenium')


def download(link):
    logger.info("selenium start connection")
    try:
        driver = webdriver.Remote(
                desired_capabilities=DesiredCapabilities.FIREFOX,
                command_executor="http://%s:4444" % SELENIUM_GRID_HOST
            )
    except Exception as e:
        logger.warning("selenium не подключился")
        return None
    logger.info("selenium connect")
    driver.get(link)
    sleep(selsleep)
    html = driver.page_source
    return html



if __name__ == "__main__":
    print(download('https://www.ozon.ru/product/tabletki-dlya-posudomoechnyh-mashin-synergetic-besfosfatnye-55-sht-55-sht-181952391/reviews/'))
