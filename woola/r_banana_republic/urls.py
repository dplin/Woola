# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from rest_framework import routers, serializers, viewsets
from r_banana_republic.views import BananaRepublicViewSet

router = routers.DefaultRouter()
router.register(r'banana_republic_items', GapViewSet)

urlpatterns = patterns('',
   url(r'^', include(router.urls)),
)




