# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-14 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_auto_20180614_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cover_pic',
            field=models.ImageField(default='pic_folder/None/no-img.png', upload_to='pic_folder/', verbose_name='coverpic'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='pic_folder/None/no-img.png', upload_to='pic_folder/', verbose_name='profilepic'),
        ),
    ]
