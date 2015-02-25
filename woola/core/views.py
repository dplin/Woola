from django.shortcuts import render
#from retailers.models import Retailer
# Load app specific settings
from django.apps import apps

from django.conf import settings
from django.db.models import get_model
from r_gap.models import Item

# Create your views here.
def index(request):
    # Get all installed applications
    all_installed_apps = apps.get_models()

    # Only models with "retailer_name" method will get selected.  "retailer_name" method is an indicator that this app is a Retailer app.
    all_retailers = filter(lambda app: 'retailer_name' in dir(app), all_installed_apps)
    retailers = sorted(all_retailers, key=lambda app: app.retailer_name)

    return render(request, 'core/home.html', locals())

def retailer(request, slug):
    #get_object_or_404(Retailer, slug=slug)
    return render(request, 'core/retailer.html', locals())
