# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tshirt_contest', '0004_poll'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='design',
            field=models.ForeignKey(default=1, to='tshirt_contest.Design'),
            preserve_default=False,
        ),
    ]
