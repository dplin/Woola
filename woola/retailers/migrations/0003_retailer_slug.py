# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('retailers', '0002_retailer_retailer_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='retailer',
            name='slug',
            field=models.SlugField(unique=True, default='k'),
            preserve_default=True,
        ),
    ]
