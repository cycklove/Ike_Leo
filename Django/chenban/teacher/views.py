from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

'''
视图函数需要有一个参数 类型应该是 HttpRequest
'''
def do_normalmap(request):
    return HttpResponse("This is normalmap")

def withparam(request,year,month):
    return HttpResponse("This is with param {0},{1}".format(year,month))

def do_app(r):
    return HttpResponse("这是个子路由")

def do_param2(r,pn):
    return HttpResponse("Page number is {0}".format(pn))