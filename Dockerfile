FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install flask flask-classy SQLAlchemy
RUN apt-get install locales
RUN echo "ja_JP UTF-8" > /etc/locale.gen
RUn locale-gen
