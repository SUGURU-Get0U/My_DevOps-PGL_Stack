# syntax=docker/dockerfile:1
FROM python:3.12-slim  
# Builds an image with the Python 3.12 image

WORKDIR /Devops-PGL_STACK

ENV FLASK_TEST=app.py

ENV FLASK_RUN_HOST=0.0.0.0

RUN apt-get update && apt-get install -y gcc  
# Installs `gcc` and other dependencies

COPY requirements.txt .
# Brings the requirements to Docker enviroment

RUN pip install -r requirements.txt  
# Installs the Python dependencies

COPY . .

EXPOSE 5000
# default docker and flask port

CMD ["flask", "run", "--debug"]