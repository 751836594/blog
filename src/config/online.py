#!/usr/bin/env python
# encoding: utf-8

"""
@version: 3.6
@author: steven
@license: Apache Licence 
@contact: 751836594@qq.com
@site: 
@software: PyCharm
@file: online.py
@time: 2017/12/13 下午2:01
"""
from logging.config import dictConfig
from os.path import abspath, dirname

import logging

import time

db_config = {
    'host': '172.17.0.3',
    'db': 'blog',  # www
    'user': 'root',
    'passwd': 'lujunwen945..',
    'charset': 'utf8',
    'port': 3306,
}

AUTH_LIST = {
    'qq': {
        "APPID": '101365196',
        "APPKey": '35273c6f7c8a4ce8641eb1cae2737e00',
        "REDIRECTURI": 'http://www.lujunwen.com/site/auth',
    }
}

HOST = 'http://www.lujunwen.com'

db_uri = 'mysql+mysqldb://%s:%s@%s:%s/%s?charset=utf8' % (
    db_config['user'],
    db_config['passwd'],
    db_config['host'],
    db_config['port'],
    db_config['db'],
)

db_params = dict(
    echo=False,
    echo_pool=True,
    encoding=db_config['charset'],
    pool_recycle=1800,  # 数据库链接时间
    pool_size=20,
    logging_name='sqlalchemy',

)

BASE_PATH = abspath(dirname(abspath(__file__)) + "/../../")

# 日志配置
logging_config = dict(
    version=1,
    formatters={
        'f': {
            'format': '%(asctime)s %(name)s [mod=%(module)s.%(funcName)s:%(lineno)d] %(process)d %(levelname)-8s   %(message)s'},
        'file_format': {
            'format': '%(asctime)s %(name)s [mod=%(module)s.%(funcName)s:%(lineno)d] [pid=%(process)d] %(levelname)-8s %(message)s'
        },
        'alert': {
            'format': '%(asctime)s %(name)s [mod=%(module)s.%(funcName)s:%(lineno)d:%(pathname)s] [pid=%(process)d] %(levelname)-8s %(message)s'
        },
    },
    handlers={
        'std': {
            'class': 'logging.StreamHandler',
            'formatter': 'f',
            'level': logging.DEBUG},
        'file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'file_format',
            'when': 'D',
            'filename': BASE_PATH + '/logs/app.log',
            'level': logging.DEBUG},
        'file_app_web': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'file_format',
            'when': 'D',
            'filename': BASE_PATH + '/logs/file_app_web-%s.log' % (
                time.strftime('%Y-%m-%d', time.localtime(time.time()))),
            'level': logging.DEBUG,
        },
    },
    loggers={
        'app_web': {
            'level': logging.DEBUG,
            'handlers': ['std', 'file', 'file_app_web'],
        },

    }
)


def log_conf(n=''):
    dictConfig(logging_config)


# logging.basicConfig(level=logging.DEBUG)
log_conf()
