from django.conf.urls import patterns, include, url
import account
from account.views import login as account_login
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	# url(r'^main/', account.views.account_main),
	# 	url(r'^main/', include('timeline.urls'))

    url(r'^admin/', include(admin.site.urls)),
	url(r'^account/', include('account.urls')),
	url(r'^$', account_login),
	url(r'^timeline/', include('timeline.urls')),
	url(r'^main/', include('account.urls')),
	url(r'^comment/', include('comment.urls'))
)

