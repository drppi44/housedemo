# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 8, 7, 30, 3, 728435, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='house',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 8, 7, 30, 12, 464034, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='flat',
            name='wc_type',
            field=models.CharField(max_length=1, choices=[('1', '\u0421\u043e\u0432\u043c\u0435\u0441\u0442\u043d\u044b\u0439'), ('2', '\u0420\u0430\u0437\u0434\u0435\u043b\u044c\u043d\u044b\u0439')]),
        ),
    ]
