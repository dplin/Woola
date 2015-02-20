from django.db import models

from retailers.models import CommonItemInfo

# Create your models here.
class Item(CommonItemInfo):
    item_image = models.ImageField(upload_to = 'retailer/r_gap', default = 'retailer/r_gap/no-img.jpg')

    def __str__(self):
        return 'test'
