from django.shortcuts import render

from retailers.models import Retailer

# Create your views here.
def index(request):
    return render(request, 'core/home.html', locals())
