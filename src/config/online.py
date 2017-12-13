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

db_config = {
    'host': '172.17.0.2',
    'db': 'blog',  # www
    'user': 'root',
    'passwd': 'lujunwen',
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
