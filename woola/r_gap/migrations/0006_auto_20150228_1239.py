# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('r_gap', '0005_auto_20150221_1541'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['pub_date']},
        ),
        migrations.RemoveField(
            model_name='item',
            name='item_title',
        ),
        migrations.AddField(
            model_name='item',
            name='item_price',
            field=models.DecimalField(max_digits=6, default=0, decimal_places=2),
            preserve_default=False,
        ),
    ]
