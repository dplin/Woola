from django.apps import AppConfig
from django.utils.text import slugify

class OldNavyConfig(AppConfig):
  name = "r_old_navy"
  verbose_name = retailer_name = "Old Navy"
  retailer_url = "http://www.oldnavy.ca"
  retailer_logo_url = "r_old_navy/images/logo.jpg"
  slug = slugify(retailer_name)
