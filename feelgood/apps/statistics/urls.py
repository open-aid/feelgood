from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('feelgood.apps.statistics.views',

    url(r'^$', 'index', name='index'),

)
