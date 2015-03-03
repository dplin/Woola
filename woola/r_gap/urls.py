# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from rest_framework import routers, serializers, viewsets
from r_gap.views import GapViewSet

router = routers.DefaultRouter()
router.register(r'gap_items', GapViewSet)

urlpatterns = patterns('',
   url(r'^', include(router.urls)),
)




