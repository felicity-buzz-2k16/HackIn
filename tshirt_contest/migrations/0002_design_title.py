# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tshirt_contest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='design',
            name='title',
            field=models.CharField(default=b'Felicity Buzz 2k15', max_length=200),
        ),
    ]
