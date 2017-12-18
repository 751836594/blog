#!/usr/bin/env python
# encoding: utf-8

"""
@version: 3.6
@author: steven
@license: Apache Licence 
@contact: 751836594@qq.com
@site: 
@software: PyCharm
@file: login.py
@time: 2017/12/18 下午4:31
"""
import hashlib
import uuid
from datetime import datetime


def generate_cookie(uuid):
    uuid_split = uuid.split('-')
    s = []
    m2 = hashlib.md5()
    for key, item in enumerate(uuid_split):
        m2.update(item.encode())
        s.append(m2.hexdigest()[3:12:2])
    return ':'.join(s)


def set_login(uuid):
    """

    :param uuid:
    :return:
    """
    cookie_str = generate_cookie(uuid)
    return cookie_str
