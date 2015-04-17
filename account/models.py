# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class User_profile(models.Model):
	owner = models.ForeignKey(User)
	name = models.CharField(max_length=50) #用户名称
	adress = models.CharField(max_length=150) #用户地址
	tel = models.TextField(max_length=150) #备注
	created_at = models.DateTimeField(auto_now_add=True) #创建时间

	class Meta(object):
		db_table = 'account_customer'
		ordering = ['id',]
