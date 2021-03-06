# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-06 05:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_auto_20190305_1617'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Student_Name',
            new_name='Student_First_Name',
        ),
        migrations.AddField(
            model_name='student',
            name='Gender',
            field=models.CharField(default=222, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='Student_Last_Name',
            field=models.CharField(default=348989, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='document',
            name='Doc_File_Path',
            field=models.FileField(upload_to='files'),
        ),
    ]
