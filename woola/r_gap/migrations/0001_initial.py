# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='R_Gap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('item_name', models.CharField(max_length=120)),
                ('item_title', models.CharField(max_length=120)),
                ('item_id', models.CharField(max_length=200)),
                ('item_url', models.URLField(max_length=500)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('item_image', models.ImageField(upload_to='retailer/r_gap', default='retailer/r_gap/no-img.jpg')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
