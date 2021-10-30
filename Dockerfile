FROM python:3

WORKDIR /APP

COPY ./requirements.txt /APP
COPY ./wsgi.py /APP
COPY ./app.ini /APP
COPY ./config.py /APP
COPY ./application /APP/application

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["uwsgi", "app.ini"]