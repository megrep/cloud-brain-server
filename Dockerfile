FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3.8 python3-pip locales
RUN pip3 install flask flask-classy SQLAlchemy
RUN echo "ja_JP UTF-8" > /etc/locale.gen
RUN locale-gen
