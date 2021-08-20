1) Запустить докер контейнер
    docker run -d --name selenium -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-firefox:4.0.0-rc-1-prerelease-20210804

2) Создать сеть 
    docker network create parselen

3) Подключить к сети контейнеры
    в папке проекта docker-compose buld
    в папке проекта docker-compose up
4)
    docker network connect parselen selenium
    docker network connect parselen parser

5) при следующих запусках если код не менялся, пункты кромер 1 и 3 пропускаются

*** особое внимание ***
    сейчас не идет парсинг комментов на озоне, потому что подключение к докер - селениуму идет через раз и через раз он прогружает всю страницу

*** добавление ссылок и выгрузка данных ***

    1) добавить: localhost/links/add/ (POST) data = {"link": text}

    2) собрать данные: localhost/links/all/ (GET)
