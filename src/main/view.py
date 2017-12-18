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
import urllib
import urllib.request

from flask import redirect
from flask import render_template
from flask import request

from biz import user
from biz.auth import *
from tools.helper import create_conn
from . import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login/index')
def login():
    auth_list = get_detail()

    return render_template('login.html', auth_list=auth_list, host=HOST)


@app.route('/site/auth', methods=['POST', 'GET'])
def auth_qq():
    code = request.args.get('code')
    if not code:
        # 获取code
        code_url = get_qq_code_url()
        return redirect(code_url)
    else:
        # 获取access_token
        access_token_url = get_qq_access_token_url(code)
        resp = urllib.request.urlopen(access_token_url)
        v = resp.read().decode('utf8')
        access_token = v[13:45]

        # 获取openid
        o_url = get_qq_open_id_url(access_token)
        res = urllib.request.urlopen(o_url).read().decode()
        s_index = res.find('openid')
        start_index = s_index + 9
        end_index = s_index + 9 + 32
        openid = res[start_index:end_index]

        is_exist = user.is_exist(openid)
        if not is_exist:
            return '已存在'

        uid = user.add(openid)
        return '新增用户uid:%d' % (uid)
