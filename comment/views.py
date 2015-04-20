# -*- coding:utf-8 -*-
from datetime import datetime
from django.contrib.auth.models import User
from django.http import HttpResponse

from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext
from comment.models import Discuss
from timeline.models import Blogs


def sendcomment(request):
	blog_id = request.POST.get('blog_id')

	if request.POST:
		user = request.user
		comment_content = request.POST.get('comment_content')
		creat_at = datetime.now()
		Discuss.objects.create(
			comment_content = comment_content,
			comment_creat_at = creat_at,
			comment_user = user.username,
			comment_id = blog_id
		)
		return HttpResponse('200')
	elif request.GET:
		return HttpResponse('200')
	else:
		return HttpResponse('500')
#
# def comment_list(request):
# 	user=request.user
# 	Discuss.objects.filter(comment=)
# 	# if request.POST:
# 	# 	owner = request.user
# 	# 	user_id = User.objects.get(user_id=owner.id)
# 	# 	comment_list = Blogs.objects.filter(comment_id=user_id)
# 	# 	c = RequestContext(request, {
# 	# 		'comment_list': comment_list
# 	# 	})
# 		return render_to_response('main.html', c)