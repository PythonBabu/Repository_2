# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-05 10:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20190305_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='Doc_File_Path',
            field=models.FilePathField(path='D:/DjangoD/March5Project\\media'),
        ),
    ]