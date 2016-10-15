# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-15 06:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('crated_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]