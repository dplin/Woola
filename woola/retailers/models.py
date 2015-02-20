from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Retailer(models.Model):
    retailer_name = models.CharField(max_length=120, null=False, blank=False)
    retailer_url = models.URLField(max_length=500, null=False, blank=False)
    retailer_image = models.ImageField(upload_to = 'retailer/', default = 'retailer/no-img.jpg')
    slug = models.SlugField(unique=True)
    pub_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.retailer_name

class CommonItemInfo(models.Model):
    item_name = models.CharField(max_length=120, null=False, blank=False)
    item_title = models.CharField(max_length=120, null=False, blank=False)
    item_image = models.ImageField(upload_to = 'retailer/' + User._meta.app_label, default = 'retailer/'+User._meta.app_label+'/no-img.jpg')
    item_id = models.CharField(max_length=200, null=False, blank=False)
    item_url = models.URLField(max_length=500, null=False, blank=False)
    pub_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True
