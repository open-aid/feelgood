from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('feelgood.apps.tools.views',

    url(r'^$', 'index', name='index'),

    url(r'^bdc/$', 'bdc.index', name='bdc-index'),
    url(r'^bdc/new/$', 'bdc.create', name='bdc-create'),
    url(r'^bdc/(?P<id>\d+)/$', 'bdc.view', name='bdc-view'),
    url(r'^bdc/(?P<id>\d+)/delete/$', 'bdc.delete', name='bdc-delete'),

    url(r'^twocolumn/$', 'twocolumn.index', name='twocolumn-index'),
    url(r'^twocolumn/new/$', 'twocolumn.create', name='twocolumn-create'),
    url(r'^twocolumn/(?P<id>\d+)/$', 'twocolumn.view', name='twocolumn-view'),
    url(r'^twocolumn/(?P<id>\d+)/delete/$', 'twocolumn.delete', name='twocolumn-delete'),

    url(r'^triplecolumn/$', 'triplecolumn.index', name='triplecolumn-index'),
    url(r'^triplecolumn/new/$', 'triplecolumn.create', name='triplecolumn-create'),
    url(r'^triplecolumn/(?P<id>\d+)/$', 'triplecolumn.view', name='triplecolumn-view'),
    url(r'^triplecolumn/(?P<id>\d+)/delete/$', 'triplecolumn.delete', name='triplecolumn-delete'),

    url(r'^das/$', 'das.index', name='das-index'),
    url(r'^das/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$', 'das.view', name='das-view'),
    url(r'^das/(?P<id>\d+)/delete/$', 'das.delete', name='das-delete'),

    url(r'^nas/$', 'nas.index', name='nas-index'),
    url(r'^nas/new/$', 'nas.create', name='nas-create'),
    url(r'^nas/(?P<id>\d+)/$', 'nas.view', name='nas-view'),
    url(r'^nas/(?P<id>\d+)/delete/$', 'nas.delete', name='nas-delete'),

    url(r'^aps/$', 'aps.index', name='aps-index'),
    url(r'^aps/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$', 'aps.view', name='aps-view'),
    url(r'^aps/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/delete/$', 'aps.delete', name='aps-delete'),
    url(r'^aps/entry/(?P<id>\d+)/delete/$', 'aps.delete_entry', name='aps-delete-entry'),

)
