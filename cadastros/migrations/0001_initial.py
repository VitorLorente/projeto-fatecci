# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 22:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('celular', models.CharField(blank=True, max_length=11, null=True)),
            ],
            options={
                'db_table': 'ALUNO',
            },
            bases=('autentication.usuario',),
        ),
        migrations.CreateModel(
            name='Coordenador',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('celular', models.CharField(blank=True, max_length=11, null=True)),
            ],
            options={
                'db_table': 'COORDENADOR',
            },
            bases=('autentication.usuario',),
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=5, unique=True)),
                ('nome', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'CURSO',
            },
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_column='nome_disciplina', max_length=240, unique=True)),
                ('carga_horaria', models.SmallIntegerField()),
                ('teoria', models.DecimalField(decimal_places=0, max_digits=3)),
                ('pratica', models.DecimalField(decimal_places=0, max_digits=3)),
                ('ementa', models.TextField(blank=True, null=True)),
                ('competencias', models.TextField(blank=True, null=True)),
                ('habilidades', models.TextField(blank=True, null=True)),
                ('conteudo', models.TextField(blank=True, null=True)),
                ('bibliografia_basica', models.TextField(blank=True, null=True)),
                ('bibliografia_complementar', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=20)),
                ('sigla_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.Curso')),
            ],
            options={
                'db_table': 'DISCIPLINA',
            },
        ),
        migrations.CreateModel(
            name='DisciplinaOfertada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.SmallIntegerField()),
                ('semestre', models.CharField(max_length=1)),
                ('nome_disciplina', models.ForeignKey(db_column='nome_disciplina', on_delete=django.db.models.deletion.DO_NOTHING, to='cadastros.Disciplina', unique=True)),
            ],
            options={
                'db_table': 'DISCIPLINA_OFERTADA',
            },
        ),
        migrations.CreateModel(
            name='GradeCurricular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.SmallIntegerField()),
                ('semestre', models.CharField(max_length=1)),
                ('sigla_curso', models.ForeignKey(db_column='sigla_curso', on_delete=django.db.models.deletion.DO_NOTHING, to='cadastros.Curso')),
            ],
            options={
                'db_table': 'GRADE_CURRICULAR',
            },
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano_ofertado', models.ForeignKey(db_column='ano_ofertado', on_delete=django.db.models.deletion.DO_NOTHING, related_name='ano_ofertado_matricula', to='cadastros.DisciplinaOfertada')),
            ],
            options={
                'db_table': 'MATRICULA',
            },
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.SmallIntegerField()),
                ('ano_grade', models.ForeignKey(db_column='ano_grade', on_delete=django.db.models.deletion.DO_NOTHING, related_name='ano_periodo', to='cadastros.GradeCurricular')),
                ('semestre_grade', models.ForeignKey(db_column='semestre_grade', on_delete=django.db.models.deletion.DO_NOTHING, related_name='semestre_periodo', to='cadastros.GradeCurricular')),
                ('sigla_curso', models.ForeignKey(blank=True, db_column='sigla_curso', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cadastros.Curso')),
            ],
            options={
                'db_table': 'PERIODO',
            },
        ),
        migrations.CreateModel(
            name='PeriodoDisciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano_grade', models.ForeignKey(db_column='ano_grade', on_delete=django.db.models.deletion.DO_NOTHING, related_name='ano_periodo_disciplina', to='cadastros.GradeCurricular')),
                ('nome_disciplina', models.ForeignKey(db_column='nome_disciplina', on_delete=django.db.models.deletion.DO_NOTHING, to='cadastros.Disciplina')),
                ('numero_periodo', models.ForeignKey(db_column='numero_periodo', on_delete=django.db.models.deletion.DO_NOTHING, to='cadastros.Periodo')),
                ('semestre_grade', models.ForeignKey(db_column='semestre_grade', on_delete=django.db.models.deletion.DO_NOTHING, related_name='semestre_periodo_disciplina', to='cadastros.GradeCurricular')),
                ('sigla_curso', models.ForeignKey(blank=True, db_column='sigla_curso', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cadastros.Curso')),
            ],
            options={
                'db_table': 'PERIODO_DISCIPLINA',
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('apelido', models.CharField(max_length=30, unique=True)),
                ('celular', models.CharField(blank=True, max_length=11, null=True)),
            ],
            options={
                'db_table': 'PROFESSOR',
            },
            bases=('autentication.usuario',),
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_turma', models.CharField(max_length=1, unique=True)),
                ('ano_ofertado', models.ForeignKey(db_column='ano_ofertado', on_delete=django.db.models.deletion.DO_NOTHING, related_name='ano_turma', to='cadastros.DisciplinaOfertada')),
                ('nome_disciplina', models.ForeignKey(db_column='nome_disciplina', on_delete=django.db.models.deletion.DO_NOTHING, related_name='nome_disciplina_turma', to='cadastros.DisciplinaOfertada')),
                ('ra_professor', models.ForeignKey(db_column='ra_professor', on_delete=django.db.models.deletion.DO_NOTHING, to='cadastros.Professor')),
                ('semestre_ofertado', models.ForeignKey(db_column='semestre_ofertado', on_delete=django.db.models.deletion.DO_NOTHING, related_name='semestre_turma', to='cadastros.DisciplinaOfertada')),
            ],
            options={
                'db_table': 'TURMA',
            },
        ),
        migrations.AddField(
            model_name='matricula',
            name='id_turma',
            field=models.ForeignKey(db_column='id_turma', on_delete=django.db.models.deletion.DO_NOTHING, to='cadastros.Turma'),
        ),
        migrations.AddField(
            model_name='matricula',
            name='nome_disciplina',
            field=models.ForeignKey(db_column='nome_disciplina', on_delete=django.db.models.deletion.DO_NOTHING, related_name='nome_disciplina_matricula', to='cadastros.DisciplinaOfertada'),
        ),
        migrations.AddField(
            model_name='matricula',
            name='ra_aluno',
            field=models.ForeignKey(db_column='ra_aluno', on_delete=django.db.models.deletion.DO_NOTHING, to='cadastros.Aluno'),
        ),
        migrations.AddField(
            model_name='matricula',
            name='semestre_ofertado',
            field=models.ForeignKey(db_column='semestre_ofertado', on_delete=django.db.models.deletion.DO_NOTHING, related_name='semestre_ofertado_matricula', to='cadastros.DisciplinaOfertada'),
        ),
        migrations.AddField(
            model_name='coordenador',
            name='sigla_curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.Curso'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='sigla_curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.Curso'),
        ),
    ]
