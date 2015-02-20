# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('retailers', '0004_auto_20150220_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retailer',
            name='slug',
            field=models.SlugField(default='a', unique=True),
            preserve_default=True,
        ),
    ]
