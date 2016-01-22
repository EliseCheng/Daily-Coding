from django.conf.urls import patterns, url
urlpatterns = patterns('swift.views',
    url(r'^index/$', 'index', name='index'),
)
