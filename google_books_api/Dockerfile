FROM python:3.8-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

RUN apk update \
    && apk add --virtual build-essential gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN adduser -D myuser
USER myuser

CMD gunicorn api.wsgi:application --bind 0.0.0.0:$PORT

# EXPOSE 8000

# CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "api.wsgi:application"]