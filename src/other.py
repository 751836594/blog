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
@time: 2017/12/13 上午10:44
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/test')
def test():
    return render_template('single.html')
