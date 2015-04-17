from django.conf.urls import patterns, include, url
from account.views import login, register, account_main


urlpatterns = patterns('',
    #url(r'^login/',index),
	url(r'^login/', login),
	url(r'^register/', register),
	url(r'^homepage/', account_main)
)

