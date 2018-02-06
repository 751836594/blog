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

from tools.db_helper import *


# conn = create_conn()


def is_exist(qq_open_id):
    """
    是否存在
    :param qq_open_id:
    :return:
    """
    status = False
    sql = '''select * from user where qq_open_id =%s'''
    params = [qq_open_id]
    with DbHelper() as conn:
        result = select_one(conn, sql, params)

    if result:
        status = True

    return {'status': status, 'result': result}


def add(qq_open_id):
    """
    加入用户
    :param qq_open_id:
    :return:
    """
    uuid_str = uuid.uuid1()
    params = {
        'qq_open_id': qq_open_id,
        'uuid': uuid_str,
        'create_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%d:%m'),
        'last_login_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%d:%m'),
    }
    with DbHelper() as conn:
        uid = insert_row(conn, 'user', params)
        return {'uid': uid, 'uuid': uuid_str}
