# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.ImageField(default='/static/images/no_image.png', upload_to='images/photos/')),
                ('region', models.CharField(max_length=100)),
                ('town', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('level', models.PositiveIntegerField()),
                ('max_level', models.PositiveIntegerField()),
                ('rooms', models.PositiveIntegerField()),
                ('area_total', models.PositiveIntegerField()),
                ('area_living', models.PositiveIntegerField()),
                ('kitchen_area', models.PositiveIntegerField()),
                ('wc_type', models.CharField(max_length=1, choices=[('1', '\u0421\u043e\u0432\u043c\u0435\u0441\u043d\u044b\u0439'), ('2', '\u0420\u0430\u0437\u0434\u0435\u043b\u044c\u043d\u044b\u0439')])),
                ('owners_count', models.PositiveIntegerField(null=True)),
                ('price', models.DecimalField(max_digits=20, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.ImageField(default='/static/images/no_image.png', upload_to='images/photos/')),
                ('region', models.CharField(max_length=100)),
                ('town', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('area_total', models.PositiveIntegerField()),
                ('levels', models.PositiveIntegerField()),
                ('price', models.DecimalField(max_digits=20, decimal_places=2)),
            ],
        ),
    ]
