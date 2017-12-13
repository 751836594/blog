#!/usr/bin/env python
# encoding: utf-8

"""
@version: 3.6
@author: steven
@license: Apache Licence 
@contact: 751836594@qq.com
@site: 
@software: PyCharm
@file: user.py
@time: 2017/12/13 下午9:24
"""
import datetime
import uuid

from tools.helper import create_conn, get_new_db, insert_rs

conn = create_conn()


def is_exist(qq_open_id):
    """
    是否存在
    :param qq_open_id:
    :return:
    """
    status = False
    sql = '''select * from user where qq_open_id =:qq_open_id'''
    params = {'qq_open_id': qq_open_id}
    with get_new_db() as db:
        result = db.execute(sql, params).fetchone()

    if result:
        status = True

    return status


def add(qq_open_id):
    """
    加入用户
    :param qq_open_id:
    :return:
    """
    params = {
        'qq_open_id': qq_open_id,
        'uuid': uuid.uuid1(),
        'create_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%d:%m'),
        'last_login_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%d:%m'),
    }

    uid = insert_rs(conn, 'user', params)
    return uid
