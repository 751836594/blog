FROM docker.8gongli.com:5000/base-python3:alpine-dev
MAINTAINER steven "lujunwen@wealink.com"

# pip install
ADD ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt &&  rm -rf /root/.cache

ENV PYTHONPATH /blog/src

ENV PROJECT_SRC = /blog/src

WORKDIR /blog
