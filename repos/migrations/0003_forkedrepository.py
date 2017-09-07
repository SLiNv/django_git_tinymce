# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-07 17:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repos', '0002_auto_20170806_0127'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForkedRepository',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fork', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repos.Repository')),
                ('original', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='original_repo', to='repos.Repository')),
            ],
        ),
    ]
