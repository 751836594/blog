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
import json
import urllib
import urllib.request

from flask import redirect
from flask import render_template
from flask import request

from biz.auth import *
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
    auth_list = get_detail('qq')
    code = request.args.get('code')
    auth_list = get_detail('qq')
    code = request.args.get('code')
    if not code:
        get_code_url = 'https://graph.qq.com/oauth2.0/authorize?response_type=code&client_id=%s&redirect_uri=%s' % (
            auth_list['APPID'], auth_list['REDIRECTURI'])
        return redirect(get_code_url)
    else:
        get_access_token_url = 'https://graph.qq.com/oauth2.0/token?grant_type=authorization_code&client_id=%s&client_secret=%s&code=%s&redirect_uri=%s' % (
            auth_list['APPID'], auth_list['APPKey'], code, auth_list['REDIRECTURI'])
        resp = urllib.request.urlopen(get_access_token_url)
        access_token = resp.read()[13:45]
        get_open_id_url = "https://graph.qq.com/oauth2.0/me?access_token=%s" % (access_token)
        res = urllib.request.urlopen(get_open_id_url).read()
        return json.dumps({'resp': resp.read(), 'access_token': access_token, 'res': res})
