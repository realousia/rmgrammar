# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-13 05:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ramyeon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('company', models.CharField(max_length=64)),
                ('sort', models.IntegerField(default=1)),
                ('size', models.IntegerField(default=0)),
                ('calories', models.IntegerField(default=0)),
            ],
        ),
    ]
