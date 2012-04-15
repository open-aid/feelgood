from django.conf.urls.defaults import patterns, include, url

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^tools/',    include('feelgood.apps.tools.urls',     namespace='tools')),

    url(r'^stats/',    include('feelgood.apps.statistics.urls', namespace='statistics')),
  
    url(r'^',          include('feelgood.apps.landing.urls',   namespace='landing')),
)

urlpatterns += staticfiles_urlpatterns()
