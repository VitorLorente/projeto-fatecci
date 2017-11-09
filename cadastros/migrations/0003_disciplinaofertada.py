# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-08 19:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0002_disciplina_professor'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisciplinaOfertada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.SmallIntegerField(unique=True)),
                ('semestre', models.CharField(max_length=1, unique=True)),
                ('nome_disciplina', models.ForeignKey(db_column='nome_disciplina', on_delete=django.db.models.deletion.DO_NOTHING, to='cadastros.Disciplina', unique=True)),
            ],
            options={
                'db_table': 'DISCIPLINA_OFERTADA',
            },
        ),
    ]
