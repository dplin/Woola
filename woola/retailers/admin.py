from django.contrib import admin
from retailers.models import Retailer

# Register your models here.

# Customize Admin
class RetailerAdmin(admin.ModelAdmin):
    list_display = ('retailer_name', 'retailer_url', 'pub_date', 'updated')

# Register your models here.
models = [Retailer]
admin.site.register(models, RetailerAdmin)

