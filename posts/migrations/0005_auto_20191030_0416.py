# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-30 02:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20191028_0556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design', models.IntegerField(blank=True, default=0)),
                ('usability', models.IntegerField(blank=True, default=0)),
                ('content', models.IntegerField(blank=True, default=0)),
                ('overall_score', models.IntegerField(blank=True, default=0)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Profile')),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='content',
        ),
        migrations.RemoveField(
            model_name='project',
            name='design',
        ),
        migrations.RemoveField(
            model_name='project',
            name='overall_score',
        ),
        migrations.RemoveField(
            model_name='project',
            name='usability',
        ),
        migrations.AddField(
            model_name='review',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Project'),
        ),
    ]
