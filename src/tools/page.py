#!/usr/bin/env python
# encoding: utf-8

"""
@version: 3.6
@author: steven
@license: Apache Licence 
@contact: 751836594@qq.com
@site: 
@software: PyCharm
@file: page.py
@time: 2018/2/1 下午3:33
"""
import math


def format_page(page, limit, total):
    """

    :param page:
    :param limit:
    :param total:
    :return:
    """
    total_page = math.ceil(total / limit)
    current_page = page
    if page >= total_page:
        next_page = page
        current_page = total_page
    else:
        next_page = page + 1

    if page <= 0:
        prev_page = 1
        current_page = 1
    else:
        prev_page = page - 1

    res = {
        'prev_page': prev_page,
        'next_page': next_page,
        'current_page': current_page,
        'total_page': total_page
    }

    return res
