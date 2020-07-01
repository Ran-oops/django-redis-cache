# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.views.decorators.cache import cache_page

from django.views.decorators.cache import cache_page
from django.shortcuts import HttpResponse
import datetime

# 加装饰器（设置时间，单位：秒）
@cache_page(60*10)
def chche1(request):
    return HttpResponse('缓存测试')
    
@cache_page(60*10)
def chche2(request):
    start=datetime.datetime.now()
    print 'kkkkkkkkkkkk'
    end=datetime.datetime.now()
    va=end-start
    print 'va', va
    return HttpResponse('缓存测试')
    

from django.core.cache import cache     # 引入缓存模块

# Create your views here.

# 设置：cache.set(键， 值， 有效时间)
# 获取：cache.get(键)
# 删除：chche.delete(键)
# 清理：cache.clear()
def chche3(request):
    # 设置缓存
    #cache.set('key1', 'value1', 500)
    # 获取缓存
    # a=cache.get('key1')
    # print 'a=====', a
    # 删除某个键的缓存
    cache.delete('key1')
    # 清空缓存
    # cache.clear()
    # return render(request, 'chche.html')
    return HttpResponse('ok')