# syntax=docker/dockerfile:1

# I'm borrowing this from https://docs.docker.com/compose/gettingstarted/#step-1-set-up with some slight modifications

FROM python:3.13-slim

# Install requirements for psycopg2
RUN apt update && apt install -y \
    build-essential \
    libpq-dev

WORKDIR /code
ENV FLASK_APP=josh_weather_api.app
ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000
COPY . .
CMD ["flask", "run", "--debug"]
