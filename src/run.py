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

from main import app

if __name__ == '__main__':
    app.run('0.0.0.0', port=8001)
    app.config.from_pyfile('../config/online.py')
