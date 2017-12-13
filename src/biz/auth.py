#!/usr/bin/env python
# encoding: utf-8

"""
@version: 3.6
@author: steven
@license: Apache Licence 
@contact: 751836594@qq.com
@site: 
@software: PyCharm
@file: auth.py
@time: 2017/12/13 下午2:07
"""
from config import *


def get_detail(name=''):
    if name == '':
        auth_detail = AUTH_LIST

    else:
        auth_detail = AUTH_LIST[name]

    return auth_detail
