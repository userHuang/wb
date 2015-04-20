# -*- coding:utf-8 -*-

from django.db import models
from account.models import User_profile
from django.contrib.auth.models import User
# Create your models here.

class Blogs(models.Model):
	user = models.ForeignKey(User)
	title = models.CharField(max_length=256)  # 标题
	blog_content = models.CharField(max_length=1024)  # 博客内容
	blog_creat_at = models.DateTimeField(auto_now_add=True)  # 微博发布时间
	blog_username = models.CharField(max_length=128)  # 用户名

	class Meta(object):
		db_table = 'timeline_blogs'
		ordering = ['-id', ]

