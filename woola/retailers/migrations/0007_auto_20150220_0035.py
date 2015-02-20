# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('retailers', '0006_auto_20150220_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retailer',
            name='slug',
            field=models.SlugField(default='j', unique=True),
            preserve_default=True,
        ),
    ]
