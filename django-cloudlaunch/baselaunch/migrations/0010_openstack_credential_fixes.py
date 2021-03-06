# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-08 14:02
from __future__ import unicode_literals

from django.db import migrations, models
import fernet_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('baselaunch', '0009_location_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='openstackcredentials',
            name='tenant_name',
        ),
        migrations.AlterField(
            model_name='awscredentials',
            name='secret_key',
            field=fernet_fields.fields.EncryptedCharField(default='dummyval', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='openstackcredentials',
            name='password',
            field=fernet_fields.fields.EncryptedCharField(default='dummyval', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='openstackcredentials',
            name='project_name',
            field=models.CharField(default='dummyval', max_length=50),
            preserve_default=False,
        ),
    ]
