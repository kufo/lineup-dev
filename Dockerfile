FROM python:3.7

WORKDIR /APP

RUN useradd -m -r user && \
    chown user /APP

COPY . .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

USER user

CMD ["uwsgi", "app.ini"]