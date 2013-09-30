from django.conf.urls import patterns, include, url
from views import current_datetime, cmd_exec
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ceni.views.home', name='home'),
    # url(r'^ceni/', include('ceni.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^time/$', current_datetime),
    url(r'^cmd/$', cmd_exec),
)
