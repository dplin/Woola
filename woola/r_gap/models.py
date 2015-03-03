from django.db import models
# Load app specific settings
from django.apps import apps
# Inherit common fields
from retailers.models import CommonItemInfo
# Make sure Unicode is compatible
from django.utils.encoding import python_2_unicode_compatible
# App ViewSet. For REST API URL auto generation.


@python_2_unicode_compatible
class Item(CommonItemInfo):
    _appname = 'r_gap'

    # Class properties
    _retailer_name = apps.get_app_config(_appname).retailer_name
    _retailer_logo_url = apps.get_app_config(_appname).retailer_logo_url
    _retailer_slug = apps.get_app_config(_appname).slug

    #_retailer_viewset = import .views.GapViewSet

    # This field requires current appname as path
    item_image = models.URLField(max_length=500, default="abc.jpg")

    def __str__(self):
        # Return self
        return apps.get_app_config(_appname).retailer_name

    class Meta:
        # default ordering when obtaining lists of objects
        ordering = ['pub_date']
