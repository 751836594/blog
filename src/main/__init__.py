#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: __init__.py
@time: 2017/1/12 下午1:34
"""

from flask import Flask

app = Flask(__name__)
# 加载配置
from main import view, other
