# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agcs', '0002_auto_20170919_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='CGV',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='companies',
            name='ENV',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='companies',
            name='ESG',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='companies',
            name='QUAL',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='companies',
            name='SOC',
            field=models.CharField(max_length=15),
        ),
    ]
