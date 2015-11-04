# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tshirt_contest', '0002_design_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
