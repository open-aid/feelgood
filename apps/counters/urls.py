from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('feelgood.apps.counters.views',

    url(r'^$', 'index', name='index'),
    url(r'^new/$', 'create', name='create'),
    url(r'^(?P<id>\d+)/$', 'view', name='view'),
    url(r'^(?P<id>\d+)/count/$', 'count', name='count'),
    url(r'^(?P<id>\d+)/reset/$', 'reset', name='reset'),
    url(r'^(?P<id>\d+)/delete/$', 'delete', name='delete'),
)
