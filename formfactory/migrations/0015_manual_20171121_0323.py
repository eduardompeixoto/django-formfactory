# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-21 03:23
from __future__ import unicode_literals

from django.db import migrations

from formfactory import SETTINGS

def update_fields_and_widgets(apps, schema_editor):
    fields = {}
    for field_type, name in SETTINGS["field-types"]:
        fields[name] = field_type

    widgets = {}
    for widget_type, name in SETTINGS["widget-types"]:
        widgets[name] = widget_type
    form_fields = apps.get_model('formfactory', 'FormField')
    for field in form_fields.objects.all():
        if field.field_type:
            field.field_type = fields[field.field_type]
        if field.widget:
            field.widget = widgets[field.widget]
        field.save()

class Migration(migrations.Migration):

    dependencies = [
        ('formfactory', '0014_auto_20171127_0206'),
    ]

    # None reverse able.
    operations = [
        migrations.RunPython(update_fields_and_widgets)
    ]
