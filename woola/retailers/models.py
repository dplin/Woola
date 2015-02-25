from django.db import models

'''
class Retailer(models.Model):
    retailer_name = models.CharField(max_length=120, null=False, blank=False)
    retailer_url = models.URLField(max_length=500, null=False, blank=False)
    retailer_image = models.ImageField(upload_to = 'retailer/', default = 'retailer/no-img.jpg')
    slug = models.SlugField(unique=True)
    pub_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.retailer_name
'''
# Create @classproperty decorator
class classproperty(property):
    def __get__(self, instance, cls):
        return classmethod(self.fget).__get__(instance, cls)()

class CommonItemInfo(models.Model):
    item_name = models.CharField(max_length=120, null=False, blank=False)
    item_title = models.CharField(max_length=120, null=False, blank=False)
    item_id = models.CharField(max_length=200, null=False, blank=False)
    item_url = models.URLField(max_length=500, null=False, blank=False)
    pub_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    @classproperty
    def retailer_name(self):
        # Return retailer name
        return self._retailer_name

    @classproperty
    def retailer_logo_url(self):
        # Return logo image URL
        return self._retailer_logo_url

    @classproperty
    def retailer_slug(self):
        # Return slug
        return self._retailer_slug

    class Meta:
        abstract = True
