#!/usr/bin/env python
# encoding: utf-8

"""
@version: 3.6
@author: steven
@license: Apache Licence 
@contact: 751836594@qq.com
@site: 
@software: PyCharm
@file: other.py
@time: 2017/12/13 上午11:32
"""

from flask import render_template

from . import app


@app.route('/other')
def other_index():
    return render_template('index.html')


@app.route('/other/index')
def other_login():
    return render_template('login.html')
