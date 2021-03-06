from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import frontpage.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ainosite.views.home', name='home'),
    # url(r'^ainosite/', include('ainosite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', frontpage.views.upload),
    url(r'^upload/', frontpage.views.upload),
    url(r'^admin/', include(admin.site.urls)),
)
