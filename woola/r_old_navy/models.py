from django.db import models
# Load app specific settings
from django.apps import apps
# Inherit common fields
from retailers.models import CommonItemInfo

class Item(CommonItemInfo):
    _appname = 'r_old_navy'

    # Class properties
    _retailer_name = apps.get_app_config(_appname).retailer_name
    _retailer_logo_url = apps.get_app_config(_appname).retailer_logo_url
    _retailer_slug = apps.get_app_config(_appname).slug

    # This field requires current appname as path
    item_image = models.ImageField(upload_to = 'retailer/'+_appname, default = 'retailer/_appname/no-img.jpg')

    def __str__(self):
        # Return self
        return apps.get_app_config(_appname).retailer_name
