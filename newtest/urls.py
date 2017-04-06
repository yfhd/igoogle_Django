from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import helloworld

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'newtest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', helloworld.index),
)
