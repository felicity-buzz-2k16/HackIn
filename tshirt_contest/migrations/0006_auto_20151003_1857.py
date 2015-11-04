# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tshirt_contest', '0005_poll_design'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
