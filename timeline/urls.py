#! -*- coding:utf-8 -*-
from django.conf.urls import patterns, url
from timeline.views import send_blog

__author__ = 'Administrator'

urlpatterns = patterns('',  # url(r'^login/',index),
	url(r'^sendblog/', send_blog),
)