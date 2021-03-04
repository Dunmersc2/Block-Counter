FROM ubuntu:20.04

LABEL maintainer="ShaneForde"

RUN apt-get update -y && apt-get install -y python3-pip python-dev

EXPOSE 5000

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

#COPY ./app /app

#ENTRYPOINT [ "python3" ]
#CMD [ "app.py" ]
ENTRYPOINT FLASK_ENV=development FLASK_APP=/app/app.py flask run --host=0.0.0.0