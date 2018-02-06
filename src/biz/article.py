#!/usr/bin/env python
# encoding: utf-8

"""
@version: 3.6
@author: steven
@license: Apache Licence 
@contact: 751836594@qq.com
@site: 
@software: PyCharm
@file: article.py
@time: 2018/2/1 上午11:37
"""
from tools.db_helper import *


def article_list(page, limit=10):
    """
    获取文章列表
    :return:
    """
    if not page:
        page = 1

    offset = (page - 1) * limit

    with DbHelper() as conn:
        sql = "select  * from article  limit %s,%s "
        params = [offset, limit]
        result_list = select_all(conn, sql, params)

        total_sql = "select FOUND_ROWS() as cnt"
        total_res = select_one(conn, total_sql);

        res = {
            'result_list': result_list,
            'total': total_res['cnt']
        }

        return res


def get_last_article(limit):
    with DbHelper() as conn:
        sql = "select SQL_CALC_FOUND_ROWS * from article  ORDER by id desc limit %s  "
        params = [limit]
        result_list = select_all(conn, sql, params)

        return result_list


def get_type():
    with DbHelper() as conn:
        sql = "select  DISTINCT type from article "
        result_list = select_all(conn, sql)
        return result_list
