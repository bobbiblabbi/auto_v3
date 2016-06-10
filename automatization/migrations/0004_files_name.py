# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('automatization', '0003_auto_20160607_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='name',
            field=models.CharField(default='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435', max_length=50),
        ),
    ]
