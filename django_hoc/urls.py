from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_hoc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'polls.views.index'),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)
