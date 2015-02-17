from django.db import models

# Create your models here.
class Retailer(models.Model):
    retailer_name = models.CharField(max_length=120, null=False, blank=False)
    retailer_url = models.CharField(max_length=200, null=False, blank=False)
    pub_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.retailer_name
