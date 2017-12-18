#!/usr/bin/env python
# encoding: utf-8

"""
@version: 3.6
@author: steven
@license: Apache Licence 
@contact: 751836594@qq.com
@site: 
@software: PyCharm
@file: auth.py
@time: 2017/12/13 下午2:07
"""
from config import *


def get_detail(name=''):
    if name == '':
        auth_detail = AUTH_LIST

    else:
        auth_detail = AUTH_LIST[name]

    return auth_detail


def get_qq_code_url():
    auth_list = get_detail('qq')
    url = 'https://graph.qq.com/oauth2.0/authorize?response_type=code&client_id=%s&redirect_uri=%s' % (
        auth_list['APPID'], auth_list['REDIRECTURI'])

    return url


def get_qq_access_token_url(code):
    return ''


def get_qq_open_id_url(access_token):
    url = "https://graph.qq.com/oauth2.0/me?access_token=%s" % (access_token)
    return url
