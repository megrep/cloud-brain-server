FROM archlinux:latest

RUN pacman -Syu --noconfirm python python-pip
RUN pip install flask flask-classy SQLAlchemy python-dateutil
RUN echo "ja_JP UTF-8" > /etc/locale.gen
#RUN locale-gen

RUN pacman -S --noconfirm julius
