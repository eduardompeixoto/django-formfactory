# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-06-28 11:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formfactory', '0010_add_clean_methods_to_forms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formfield',
            name='label',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
