# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('r_gap', '0007_auto_20150301_0323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_id',
            field=models.CharField(null=True, max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='item_name',
            field=models.CharField(null=True, max_length=120),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='item_price',
            field=models.DecimalField(decimal_places=2, null=True, max_digits=6),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='item_url',
            field=models.URLField(null=True, max_length=500),
            preserve_default=True,
        ),
    ]
