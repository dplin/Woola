# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('r_old_navy', '0002_auto_20150220_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.ImageField(default='retailer/auth/no-img.jpg', upload_to='retailer/auth'),
            preserve_default=True,
        ),
    ]
