from django.shortcuts import render
from django.http import HttpResponse
# Load app specific settings
from django.apps import apps
# Helper
from django.db.models import get_model
from django.template import TemplateDoesNotExist, loader
import os.path
import json


#from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt, csrf_protect


# Create your views here.
def index(request):
    # Get all installed applications
    all_installed_apps = apps.get_models()

    # Only models with "retailer_name" method will get selected.  "retailer_name" method is an indicator that this app is a Retailer app.
    all_retailers = filter(lambda app: 'retailer_name' in dir(app), all_installed_apps)
    retailers = sorted(all_retailers, key=lambda app: app.retailer_name)

    return render(request, 'core/home.html', locals())

def retailer(request, slug):
    """
    Template path is unique to each app.
    """

    # Get all installed applications
    all_installed_apps = apps.get_models()

    # Set default template path
    template_path = '404.html'

    # Filter all non related apps and keep only Retailer apps.
    all_retailers = filter(lambda app: 'retailer_name' in dir(app), all_installed_apps)

    # Loop through all retailers object
    for retailer in all_retailers:
      # Search based on Slug
      if slug == retailer.retailer_slug:
          try:
            template = loader.get_template(retailer.app_name + '/list.html')

            # Make sure template file exist
            if template is not None:
              # Assign template path then break
              template_path = retailer.app_name + '/list.html'
              # Angular app name
              ng_app_name = '=' + retailer.retailer_name.lower() + 'App'
              break
          except TemplateDoesNotExist:
            template_path = '404.html'

    return render(request, template_path, locals())


"""
Crawler function to get item information from retailer website. Probably should put it into each Retailer app.....................since every site is a bit different......
"""
import requests
from bs4 import BeautifulSoup

class Crawler():
    def __init__(self, url):
      self.url = url

    def get_soup(self):
      source_code = requests.get(self.url)
      # Get web page source code
      plain_text = source_code.text
      # Inject into BeautifulSoup
      soup = BeautifulSoup(plain_text)

      return soup

    class Meta:
        abstract = True


class Monk(Crawler):
    def find_by_class(self, soup, cname):
      for link in soup.find_all(cname):
          print(link.get('href'))

@csrf_protect
def crawler(request):
    cr = Monk(request.GET['url'])
    soup = cr.get_soup()
    cr.find_by_class(soup, 'a')




    data = {'foo': request.GET['url'], 'hello': 'dddd'}
    return HttpResponse(json.dumps(data), content_type='application/json')
