# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arquivoquestao',
            name='arquivo',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='arquivoresposta',
            name='arquivo',
            field=models.FileField(max_length=500, unique=True, upload_to=''),
        ),
    ]
