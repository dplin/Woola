from django.apps import AppConfig
from django.utils.text import slugify

class AmericanEagleOutfittersConfig(AppConfig):
  name = "r_american_eagle_outfitters"
  verbose_name = retailer_name = "American Eagle Outfitters"
  retailer_url = "http://www.ae.com/web/canada"
  retailer_logo_url = "r_american_eagle_outfitters/images/logo.jpg"
  slug = slugify(retailer_name)
