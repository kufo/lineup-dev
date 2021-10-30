FROM python:3

WORKDIR /APP

RUN useradd -m -r user && \
    chown user /APP

COPY . /APP


RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["uwsgi", "app.ini"]