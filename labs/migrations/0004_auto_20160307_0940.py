# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-07 09:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0003_auto_20160307_0937'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='attendees_expected',
            new_name='ticket_number',
        ),
    ]
