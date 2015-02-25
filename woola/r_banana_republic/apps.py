from django.apps import AppConfig
from django.utils.text import slugify

class BananaRepublicConfig(AppConfig):
  name = "r_banana_republic"
  verbose_name = retailer_name = "Banana Republic"
  retailer_url = "http://bananarepublic.gapcanada.ca"
  retailer_logo_url = "r_banana_republic/images/logo.jpg"
  slug = slugify(retailer_name)
