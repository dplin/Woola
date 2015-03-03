# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.apps import apps

from rest_framework import routers, serializers, viewsets


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

"""
Auto generate REST API URL for all retailers using Router
"""

#


urlpatterns = patterns('',
    url(r'^$', 'core.views.index', name='home'),
    url(r'^about/$',
        TemplateView.as_view(template_name='pages/about.html'),
        name="about"),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # User management
    url(r'^users/', include("users.urls", namespace="users")),
    url(r'^accounts/', include('allauth.urls')),

    # Uncomment the next line to enable avatars
    url(r'^avatar/', include('avatar.urls')),

    # Your stuff: custom urls go here

    # Retailers
    url(r'^retailer/', include('core.urls')),

    url(r'^api/v1/crawler/$', 'core.views.crawler', name='crawler'),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


"""
Get RESTful APIs from all Retailer apps
"""

REST_APIs = patterns('',)

# Get all installed applications
all_installed_apps = apps.get_models()

# Filter all non related apps and keep only Retailer apps.
all_retailers = filter(lambda app: 'retailer_name' in dir(app), all_installed_apps)

# Loop through all retailers object
for retailer in all_retailers:
    # Create URL pattern
    url_pattern = url(r'^api/v1/', include(retailer.app_name + '.urls'))
    # Store API URL pattern in REST_APIs
    REST_APIs.append(url_pattern)

# Create final URL pattern
urlpatterns += REST_APIs

