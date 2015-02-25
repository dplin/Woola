# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('retailers', '0008_auto_20150220_1309'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Retailer',
        ),
    ]
