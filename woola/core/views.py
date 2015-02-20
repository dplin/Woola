from django.shortcuts import render

from retailers.models import Retailer

# Create your views here.
def index(request):
    all_retailers = Retailer.objects.all().order_by('retailer_name')[:3]
    return render(request, 'core/home.html', locals())

def retailer(request, slug):
    #get_object_or_404(Retailer, slug=slug)
    return render(request, 'core/retailer.html', locals())
