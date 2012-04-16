from django.conf.urls.defaults import patterns, include, url

from django.views.generic.simple import direct_to_template

urlpatterns = patterns('feelgood.apps.landing.views',

    url(r'^$', 'index', name='index'),
    
    url(r'about/^$', 'about', name='about'),

    url(r'^account/registration/$', 'registration', name='registration'),
    url(r'^account/login/$',        'login', name='login'),
    url(r'^account/logout/$',       'logout', name='logout'),

)
