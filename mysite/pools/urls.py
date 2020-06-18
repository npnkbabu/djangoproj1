# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$',views.index, name='index'),
    #http://127.0.0.1/pools/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    #http://127.0.0.1/pools/2
    url(r'^(?P<question_id>[0-9]+)/results$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote$', views.vote, name='vote')
    ]

