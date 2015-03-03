# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('r_gap', '0006_auto_20150228_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.URLField(default='abc.jpg', max_length=500),
            preserve_default=True,
        ),
    ]
