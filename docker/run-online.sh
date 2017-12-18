#!/usr/bin/env bash


if [ ! -n "$1" ]
then
    echo '请指定容器名称'
    echo '例如：'
    echo '    sh docker/run-online.sh blog-online'
    exit 0
fi
mkdir logs

PYTHONPATH=`pwd`/src
CONFIG_MODE_TEXT=`cat ${PYTHONPATH}/config/config_mode`


 # -d --restart=always \
 #-it --rm \
# 后台运行
docker run \
        --name $1 \
        -h $1 \
        --dns=10.1.1.75 \
        --dns=202.96.209.5 \
        --privileged \
        --cap-add SYS_PTRACE \
        \
        -v `pwd`/:/blog \
        -v `pwd`/docker/online/etc/:/blog/etc \
        -p 80:80 \
        -d --restart=always \
        blog/online \
        supervisord -c etc/supervisord.conf
