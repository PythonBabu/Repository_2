# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-15 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0006_auto_20190308_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='Doc_File_Path',
            field=models.FileField(upload_to='D:\\Django Projects\\March5Project\\testapp\\static'),
        ),
    ]