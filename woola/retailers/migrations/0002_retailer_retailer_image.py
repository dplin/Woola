# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('retailers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='retailer',
            name='retailer_image',
            field=models.ImageField(default='retailer/no-img.jpg', upload_to='retailer/'),
            preserve_default=True,
        ),
    ]
