# Dockerfile
FROM python:3.7.16
WORKDIR /fastapiProject
COPY . /fastapiProject
RUN pip install -r requirements.txt
EXPOSE 8000
