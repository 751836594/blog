#!/usr/bin/env python
# encoding: utf-8

"""
@version: 3.6
@author: steven
@license: Apache Licence 
@contact: 751836594@qq.com
@site: 
@software: PyCharm
@file: app.py
@time: 2017/11/2 下午9:05
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run('127.0.0.1', '5000')
