# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 12:44:09 2020

@author: NAIDU
"""


from django.urls import path
from . import views

urlpatterns = [
    path('<int:course_id>/',views.detail, name='details'),
    path('', views.Courses,name='home-page'),
]
