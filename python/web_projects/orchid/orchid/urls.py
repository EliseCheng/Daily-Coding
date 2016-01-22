from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'orchid.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'soil.views.index', name='index'),
    url(r'^upload/$', 'soil.views.upload', name='upload'),
    url(r"^swift/", include("swift.urls", app_name='swift'))
)
