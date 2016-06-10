# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('automatization', '0005_auto_20160609_1332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coorx1', models.CharField(max_length=4)),
                ('coory1', models.CharField(max_length=4)),
                ('text1', models.CharField(max_length=100)),
                ('coorx2', models.CharField(max_length=4)),
                ('coory2', models.CharField(max_length=4)),
                ('text2', models.CharField(max_length=100)),
                ('coorx3', models.CharField(max_length=4)),
                ('coory3', models.CharField(max_length=4)),
                ('text3', models.CharField(max_length=100)),
                ('coorx4', models.CharField(max_length=4)),
                ('coory4', models.CharField(max_length=4)),
                ('text4', models.CharField(max_length=100)),
                ('coorx5', models.CharField(max_length=4)),
                ('coory5', models.CharField(max_length=4)),
                ('text5', models.CharField(max_length=100)),
                ('coorx6', models.CharField(max_length=4)),
                ('coory6', models.CharField(max_length=4)),
                ('text6', models.CharField(max_length=100)),
                ('coorx7', models.CharField(max_length=4)),
                ('coory7', models.CharField(max_length=4)),
                ('text7', models.CharField(max_length=100)),
                ('coorx8', models.CharField(max_length=4)),
                ('coory8', models.CharField(max_length=4)),
                ('text8', models.CharField(max_length=100)),
                ('coorx9', models.CharField(max_length=4)),
                ('coory9', models.CharField(max_length=4)),
                ('text9', models.CharField(max_length=100)),
                ('coorx10', models.CharField(max_length=4)),
                ('coory10', models.CharField(max_length=4)),
                ('text10', models.CharField(max_length=100)),
                ('which_page1', models.ForeignKey(to='automatization.Files')),
            ],
        ),
    ]
