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
import html
import urllib
import urllib.request

from datetime import timedelta, datetime

from flask import make_response
from flask import redirect
from flask import render_template
from flask import request

from biz import user, login as _login
from biz.auth import *
from biz.article import *
from biz.content import *
from . import app
from tools.page import format_page


app_log = logging.getLogger('app_web')

limit = 10


@app.before_request
def before_request():
    pass


@app.route('/')
@app.route('/article/<int:page>')
def index(page=1):
    res = article_list(page)
    if not res['result_list'] and res['total'] > 0:
        return redirect('/')

    last_article = get_last_article(5)
    type_list = get_type()
    page = format_page(page=page, limit=limit, total=res['total'])
    return render_template('index.html', result_list=res['result_list'], total=res['total'], page=page,last_article=last_article,type_list=type_list)


@app.route('/detail/<int:uuid>')
def detail(uuid):
    res = get_article_detail(uuid=uuid)
    if not res:
        return redirect('/')
    md = res['content']
    return render_template('detail.html', html=md)


@app.route('/login/index')
def login():
    auth_list = get_detail()
    uuid = request.cookies.get('uuid')
    return render_template('login.html', auth_list=auth_list, host=HOST, uuid=uuid)


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

        result = user.is_exist(openid)
        if result['status']:
            login_cookie_uuid = _login.set_login(result['result']['uuid'])
            expires_time = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S")
        else:
            add_result = user.add(openid)
            login_cookie_uuid = _login.set_login(add_result['uuid'])
            expires_time = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S")

        resp = make_response(render_template('auth.html'))
        resp.set_cookie(key='uuid', value=login_cookie_uuid, expires=expires_time, domain='www.lujunwen.com')
        return resp
