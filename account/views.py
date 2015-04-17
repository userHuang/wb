# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, Http404
from django.template import Context, RequestContext
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import render_to_response, render
from django.contrib.auth.models import User
from django.contrib import auth
from django.db.models import Q
from models import *


# ===============================================================================
# login : 登录
#===============================================================================
from timeline.models import Blogs


def login(request):
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
		if user:
			auth.login(request, user)
			# return render_to_response('main.html', {})
			return HttpResponseRedirect('/main/homepage/')

		else:
			#用户名密码错误
			c = RequestContext(request, {
			'errorMsg': u'用户名或密码错误'
			})
			return HttpResponseRedirect('/login/')
	else:
		c = RequestContext(request, {
		})
		return render_to_response('account/login.html', c)


def account_main(request):
	owner = request.user # 获取当期用户名
	user = User.objects.get(username=owner) # 当前用户id
	blog_list = Blogs.objects.filter(user=user)
	c = RequestContext(request, {
		'blog_list': blog_list
	})
	return render_to_response('main.html', c)



#===============================================================================
# register : 注册
#===============================================================================
def register(request):
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		newuser = User.objects.create_user(
			username=username,
			password=password
		)
		newuser.save()
		return HttpResponseRedirect('/account/login/')
	else:
		return render_to_response('account/register.html')
