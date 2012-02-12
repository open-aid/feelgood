from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('feelgood.apps.landing.views',

    url(r'^$', 'index', name='index'),

    url(r'^account/registration/$', 'registration', name='registration'),
    url(r'^account/login/$',        'login', name='login'),
    url(r'^account/logout/$',       'logout', name='logout'),

)
