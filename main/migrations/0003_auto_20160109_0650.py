# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20160108_0730'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='area',
            field=models.CharField(default='232', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='house',
            name='area',
            field=models.CharField(default='eqwe', max_length=100),
            preserve_default=False,
        ),
    ]
