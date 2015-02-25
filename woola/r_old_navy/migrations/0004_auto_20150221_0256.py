# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('r_old_navy', '0003_auto_20150220_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.ImageField(default='retailer/r_old_navy/no-img.jpg', upload_to='retailer/r_old_navy'),
            preserve_default=True,
        ),
    ]
