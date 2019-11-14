FROM python:3.7-buster

ENV DEBIAN_FRONTEND=noninteractive

RUN pip3 install pandas

WORKDIR /usr/share/git/modelprop
RUN mkdir output
COPY . .
