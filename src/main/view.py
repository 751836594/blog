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
@time: 2017/12/13 上午11:18
"""
from flask import render_template

from . import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login/index')
def login():
    return render_template('login.html')
