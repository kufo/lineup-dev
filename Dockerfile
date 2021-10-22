FROM python:3

WORKDIR /APP

COPY . /APP

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["uwsgi", "app.ini"]