FROM 751836594/python3
MAINTAINER steven "751836594@qq.com"

# pip install
ADD ./requirements.txt /requirements.txt
RUN $add_libs &&  pip install -r /requirements.txt && $del_libs &&  rm -rf /root/.cache
RUN apk add --no-cache mariadb-client-libs

ENV PYTHONPATH /blog/src
ENV PROJECT_SRC = /blog/src
WORKDIR /blog
