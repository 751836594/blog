#!/usr/bin/env python
# encoding: utf-8

"""
@version: 3.6
@author: steven
@license: Apache Licence 
@contact: 751836594@qq.com
@site: 
@software: PyCharm
@file: content.py
@time: 2018/2/2 下午4:49
"""
from tools.db_helper import *


def get_article_detail(uuid):
    sql = '''select * from jianshu_content where uuid =%s'''
    params = [uuid]
    with DbHelper() as conn:
        res = select_one(conn, sql, params)
        return res
