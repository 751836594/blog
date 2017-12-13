# coding:utf-8
"""
数据库助手
"""
from sqlalchemy.pool import QueuePool
from sqlalchemy.orm import sessionmaker

__author__ = 'sdm'
import logging
import sqlalchemy
from config import db_uri, db_params

log = logging.getLogger('db')
engine = sqlalchemy.create_engine(db_uri, poolclass=QueuePool, max_overflow=10, **db_params)


def create_conn():
    conn = engine.connect()
    return conn


class get_new_db(object):
    """
    获取游标 实例
    """

    def __init__(self):
        self.conn = create_conn()
        self.sessionmaker = sessionmaker(autocommit=True, autoflush=True, bind=self.conn)

    def __enter__(self):
        """
        :return:
        :type:(MySQLdb.Connection, MySQLdb.cursors.DictCursor)
        """
        self.session = self.sessionmaker()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):

        try:
            self.conn.close()
        except Exception as e:
            log.exception(e)


# 数据库工具方法

def insert_rs(rs, table, row):
    sql = 'insert into `' + table + '`'
    keys = list(row.keys())
    sql += ' (' + (', '.join(['`%s`' % k for k in keys])) + ')'
    sql += 'values(' + ', '.join(['%s' for _ in keys]) + ')'
    param = [row[k] for k in keys]
    ret = rs.execute(sql, param)
    return ret.lastrowid


def get_table_row(table, condition):
    with get_new_db() as conn:
        keys = list(condition.keys())
        where = ' and '.join('`%s`=%%s' % (k,) for k in keys)
        param = [condition[k] for k in keys]
        sql = 'select * from ' + table + ' where ' + where
        print(sql)
        return conn.execute(sql, param).fetchone()


def move_row_rs(conn, table, del_table, condition):
    """
    移动表记录到另外一个表
    :param rs:
    :param table:
    :param del_table:
    :param condition:
    :return:
    """
    keys = list(condition.keys())
    if not keys:
        log.error('error condition,empty:%s' % (str(condition),))
        return

    sql_where = ' and '.join('`%s`=%%s' % (k,) for k in keys)
    param = [condition[k] for k in keys]
    rows = conn.execute('SELECT * FROM ' + table + ' WHERE ' + sql_where, param).fetchall()
    for row in rows:
        log.debug('insert %s(%s) ' % (del_table, str(row)))
        insert_rs(conn, del_table, row)

    log.debug('delete %s(%s) ' % (table, str(param)))
    conn.execute('DELETE FROM ' + table + ' WHERE ' + sql_where, param)


def update_table_row(conn, table, cond, row):
    sql = 'update `' + table + '` set '
    keys = list(row.keys())
    sql += (', '.join(['`%s`=%%s' % k for k in keys]))
    sql += ' where '
    sql += ' and '.join(['`%s`=%%s' % k for k in list(cond.keys())])
    param = [row[k] for k in keys]
    param += [cond[k] for k in cond]
    ret = conn.execute(sql, param)
    return ret.rowcount
