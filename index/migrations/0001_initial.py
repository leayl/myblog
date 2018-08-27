# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-27 04:27
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
                ('title', models.CharField(max_length=100, verbose_name='博客标题')),
                ('category', models.CharField(blank=True, max_length=100, verbose_name='博客标签')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('update_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='更新时间')),
                ('content', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-pub_date'],
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
    ]