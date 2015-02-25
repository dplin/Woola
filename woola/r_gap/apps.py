from django.apps import AppConfig
from django.utils.text import slugify

class GapConfig(AppConfig):
  name = "r_gap"
  verbose_name = retailer_name = "Gap"
  retailer_url = "http://www.gapcanada.ca"
  retailer_logo_url = "r_gap/images/logo.jpg"
  slug = slugify(retailer_name)
