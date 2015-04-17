# -*- coding:utf-8 -*-
import datetime
from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
from comment.models import Discuss

def sendcomment(request):
	if request.POST:
		user = request.user
		comment_content = request.POST.get('comment_content')
		creat_at = datetime.now()

		Discuss.objects.create(
			comment_content = comment_content,
			comment_creat_at = creat_at,
			comment_user = user.username,
			comment_id = user.id
		)
		print 11111
		return HttpResponse('200')
	elif request.GET:
		return HttpResponse('200')
	else:
		return HttpResponse('500')