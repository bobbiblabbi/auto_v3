# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('automatization', '0004_files_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='name',
            field=models.CharField(default='Name', max_length=50),
        ),
    ]
