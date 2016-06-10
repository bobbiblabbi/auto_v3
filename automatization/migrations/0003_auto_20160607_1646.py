# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('automatization', '0002_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='upload',
            field=models.FileField(upload_to=b''),
        ),
    ]
