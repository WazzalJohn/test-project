# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 11:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_remove_user_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=264, unique=True),
        ),
    ]
