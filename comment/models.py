# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.
from django.db.models import ForeignKey
from timeline.models import Blogs


class Discuss(models.Model):
	comment_id = ForeignKey(Blogs)
	comment_content = models.CharField(max_length=1024)
	comment_creat_at = models.DateTimeField(auto_now_add=True)
	comment_user = models.CharField(max_length=256)

	class Meta(object):
		db_table = 'comment_discuss'
		ordering = ['-id',]