from django.db import models

from retailers.models import CommonItemInfo

# Create your models here.
class Item(CommonItemInfo):
#    item_image = models.ImageField(upload_to = 'retailer/' + User._meta.app_label, default = 'retailer/r_old_navy/no-img.jpg')

    def __str__(self):
        return 'test'
