#!/usr/bin/env python
# encoding: utf-8

"""
@version: 3.6
@author: steven
@license: Apache Licence 
@contact: 751836594@qq.com
@site: 
@software: PyCharm
@file: mysql.py
@time: 2018/1/29 下午4:03
"""
import logging
import pymysql.cursors
from config import db_config


log = logging.getLogger('db')


def connect():

    conn = pymysql.connect(host=db_config['host'],
                           user=db_config['user'],
                           password=db_config['passwd'],
                           db=db_config['db'],
                           charset=db_config['charset'],
                           cursorclass=pymysql.cursors.DictCursor)

    return conn


def insert_row(conn, table, row):
    sql = 'insert into `' + table + '`'
    keys = list(row.keys())
    sql += ' (' + (', '.join(['`%s`' % k for k in keys])) + ')'
    sql += 'values(' + ', '.join(['%s' for _ in keys]) + ')'
    print(sql)
    param = [row[k] for k in keys]
    print(tuple(param))
    insert_id = conn.cursor().execute(sql, param)
    conn.commit()
    return insert_id


def select_one(conn, sql, params=None):
    cur = conn.cursor()
    cur.execute(sql, params)
    res = cur.fetchone()
    return res


def select_all(conn, sql, params=None):
    cur = conn.cursor()
    cur.execute(sql, params)
    res = cur.fetchall()
    return res


class DbHelper():
    """
    获取游标 实例
    """
    def __init__(self):
        """

        """
        self.conn = connect()

    def __enter__(self):
        """
        :return:
        :type:(MySQLdb.Connection, MySQLdb.cursors.DictCursor)
        """
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        """

        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        try:
            self.conn.close()
        except Exception as e:
            log.exception(e)
