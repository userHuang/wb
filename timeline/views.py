# -*- coding:utf-8 -*-
from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from datetime import datetime
from django.template import RequestContext
from timeline.models import Blogs

def send_blog(request):
	print request.user
	if request.POST:
		owner = request.user # 获取当前用户名
		blog_content = request.POST.get('blog_content') # 获取发布微博内容
		creat_at = datetime.now()
		Blogs.objects.create(
			user=owner,
			blog_content=blog_content,
			blog_creat_at=creat_at
		)
		return HttpResponse('200')
	elif request.GET:
		return HttpResponse('200')
	else:
		return HttpResponse('500')

# def list_blog(request):
# 	if request.POST:
# 		owner = request.user # 获取当期用户名
# 		user = User.objects.get(username=owner) # 当前用户id
# 		blog_list = Blogs.objects.filter(user=user)
# 		c = RequestContext(request, {
# 			'blog_list': blog_list
# 		})
# 		return render_to_response('main.html', c)