#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/22 09:58
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : view.py
# @Software: PyCharm Community Edition

from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse,Http404
from django.shortcuts import render_to_response
import datetime
import logging
import json

logger = logging.getLogger("django") # 为loggers中定义的名称
logger2 = logging.getLogger("test2")

def hello(request):
    return HttpResponse("Hello world! 123 , 你好世界！")

def home(request):
    return HttpResponse("home page")

# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)


# def current_datetime(request):
#     now = datetime.datetime.now()
#     t = get_template('current_datetime.html')
#     html = t.render({'current_date': now})
#     return HttpResponse(html)

def current_datetime(request):
    now = datetime.datetime.now()

    # logger.debug(now)
    # logger.info(now)
    # logger.warning(now)
    logger.error(now)
    # logger.critical(now)

    # logger2.debug(now)
    # logger2.info(now)
    # logger2.warning(now)
    logger2.error(now)
    # logger2.critical(now)
    return render_to_response('current_datetime.html', {'current_date': now})
    # return render_to_response('current_datetime.html', locals())


def post_test(request):
    if request.method == 'POST':
        data = request.POST
        praseData(data)
        return HttpResponse("this is post test")
    else:
        raise Http404()

def praseData(data):
    user_str = data.get('user',None)
    if user_str:
        user_dic = json.loads(user_str)
        print(user_dic)

