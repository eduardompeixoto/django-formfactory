# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 10:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formfactory', '0012_auto_20170703_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='action',
            field=models.CharField(choices=[(b'formfactory.actions.file_upload', b'formfactory.actions.file_upload'), (b'formfactory.actions.login', b'formfactory.actions.login'), (b'formfactory.actions.send_email', b'formfactory.actions.send_email'), (b'formfactory.actions.store_data', b'formfactory.actions.store_data')], max_length=128),
        ),
        migrations.AlterField(
            model_name='customerrormessage',
            name='key',
            field=models.CharField(choices=[(b'empty', b'empty'), (b'incomplete', b'incomplete'), (b'invalid', b'invalid'), (b'invalid_choice', b'invalid_choice'), (b'invalid_image', b'invalid_image'), (b'invalid_list', b'invalid_list'), (b'invalid_date', b'invalid_date'), (b'invalid_time', b'invalid_time'), (b'invalid_pk_value', b'invalid_pk_value'), (b'list', b'list'), (b'max_decimal_places', b'max_decimal_places'), (b'max_digits', b'max_digits'), (b'max_length', b'max_length'), (b'max_value', b'max_value'), (b'max_whole_digits', b'max_whole_digits'), (b'min_length', b'min_length'), (b'min_value', b'min_value'), (b'missing', b'missing'), (b'required', b'required')], max_length=128),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='choices',
            field=models.ManyToManyField(blank=True, to='formfactory.FieldChoice'),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='field_type',
            field=models.CharField(choices=[(b'BooleanField', b'BooleanField'), (b'CharField', b'CharField'), (b'ChoiceField', b'ChoiceField'), (b'DateField', b'DateField'), (b'DateTimeField', b'DateTimeField'), (b'DecimalField', b'DecimalField'), (b'EmailField', b'EmailField'), (b'FileField', b'FileField'), (b'FloatField', b'FloatField'), (b'GenericIPAddressField', b'GenericIPAddressField'), (b'IntegerField', b'IntegerField'), (b'MultipleChoiceField', b'MultipleChoiceField'), (b'SlugField', b'SlugField'), (b'SplitDateTimeField', b'SplitDateTimeField'), (b'TimeField', b'TimeField'), (b'URLField', b'URLField'), (b'UUIDField', b'UUIDField')], max_length=128),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='widget',
            field=models.CharField(blank=True, choices=[(b'CheckboxInput', b'CheckboxInput'), (b'CheckboxSelectMultiple', b'CheckboxSelectMultiple'), (b'DateInput', b'DateInput'), (b'DateTimeInput', b'DateTimeInput'), (b'EmailInput', b'EmailInput'), (b'FileInput', b'FileInput'), (b'HiddenInput', b'HiddenInput'), (b'NullBooleanSelect', b'NullBooleanSelect'), (b'NumberInput', b'NumberInput'), (b'PasswordInput', b'PasswordInput'), (b'RadioSelect', b'RadioSelect'), (b'Select', b'Select'), (b'SelectMultiple', b'SelectMultiple'), (b'Textarea', b'Textarea'), (b'TextInput', b'TextInput'), (b'TimeInput', b'TimeInput'), (b'URLInput', b'URLInput')], help_text='Leave blank if you prefer to use the default widget.', max_length=128, null=True),
        ),
    ]