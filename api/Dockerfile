FROM python:3
WORKDIR /api
COPY /api/requirements.txt /api
RUN pip install --no-cache-dir -r requirements.txt
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
COPY /api /api
CMD ["flask", "run"]