FROM 751836594/python3
MAINTAINER steven "751836594@qq.com"
# pip install
ADD ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt &&  rm -rf /root/.cache

ENV PYTHONPATH /blog/src

ENV PROJECT_SRC = /blog/src

WORKDIR /blog
