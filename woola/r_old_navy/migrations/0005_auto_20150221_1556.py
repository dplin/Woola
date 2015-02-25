# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('r_old_navy', '0004_auto_20150221_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.ImageField(upload_to='retailer/r_old_navy', default='retailer/_appname/no-img.jpg'),
            preserve_default=True,
        ),
    ]
