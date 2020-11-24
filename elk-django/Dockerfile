FROM python:3.6.11-slim-buster

ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && apt-get install -y build-essential 

RUN mkdir /app
WORKDIR /app

COPY ./requirements/ /app/requirements/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements/production.txt

COPY . /app/

CMD ["python3", "manage.py", "runserver", "0.0.0.0:50021"]