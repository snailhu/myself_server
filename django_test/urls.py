from django.conf.urls import patterns, include, url

from django.contrib import admin
from MyselfApp.views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^captcha/', include('captcha.urls')),
    #url(r'^refresh/', refresh),
    #url(r'^some_view/', some_view),
    url(r'^upload/file/', upload_file),
    url(r'^index/', index),
    url(r'^player/', player),
)
