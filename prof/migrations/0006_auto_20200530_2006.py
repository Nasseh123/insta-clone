# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-30 17:06
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0005_image_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_caption',
            field=tinymce.models.HTMLField(),
        ),
    ]
