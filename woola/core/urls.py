# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from core import views

urlpatterns = patterns('',
   url(r'^(?P<slug>[\w-]+)/$', views.retailer, name='retailer'),
)
