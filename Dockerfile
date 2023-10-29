FROM python:3.10.12
ENV PYTHONUNBUFFERED 1
ENV NODE_OPTIONS="--openssl-legacy-provider"

WORKDIR /app

COPY app .

RUN mkdir -p app/static

RUN pip install -r requirements.txt

CMD ["uwsgi", "app_uwsgi.ini"]