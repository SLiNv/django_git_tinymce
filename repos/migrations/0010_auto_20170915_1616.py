# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-15 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repos', '0009_repository_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='culture',
            field=models.CharField(choices=[('Culture1', (('subcul1', 'sub1'), ('subcul2', 'sub2'))), ('Culture2', (('subcul1', 'subcul1'), ('subcul2', 'subcul2'))), ('Culture3', 'Culture3')], default='default', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='repository',
            name='grade_level',
            field=models.CharField(blank=True, choices=[('K', 'K'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], max_length=2),
        ),
        migrations.AddField(
            model_name='repository',
            name='subject',
            field=models.CharField(blank=True, choices=[('Subject1', (('subsub1', 'sub1'), ('subsub2', 'sub2'))), ('Subject2', (('subsub1', 'subsub1'), ('subsub2', 'subsub2'))), ('Subject3', 'Subject3')], max_length=100),
        ),
    ]
