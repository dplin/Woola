# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from core import views

urlpatterns = patterns('',
    url(
        regex=r'^$',
        view=views.index,
        name='home'
    ),
)
