#!/usr/bin/env python
# encoding: utf-8

"""
@version: 3.6
@author: steven
@license: Apache Licence 
@contact: 751836594@qq.com
@site: 
@software: PyCharm
@file: view.py
@time: 2018/1/17 下午5:49
"""

from flask import render_template


def display(html, **context):
    uuid = 1
    render_template(html, **context, uuid=uuid)