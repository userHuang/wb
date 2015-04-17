#! -*- coding:utf-8 -*-
from django.conf.urls import patterns, url
from comment.views import sendcomment

__author__ = 'Administrator'

urlpatterns = patterns('',  # url(r'^login/',index),
	url(r'^sendcomment/', sendcomment),
)