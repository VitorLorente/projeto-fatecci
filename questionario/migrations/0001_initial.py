# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 22:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArquivoQuestao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo', models.CharField(max_length=500, unique=True)),
                ('ano_ofertado', models.ForeignKey(db_column='ano_ofertado', on_delete=django.db.models.deletion.DO_NOTHING, related_name='arquivoAno_ofertado', to='cadastros.DisciplinaOfertada')),
                ('id_turma', models.ForeignKey(db_column='id_turma', on_delete=django.db.models.deletion.DO_NOTHING, related_name='arquivoId_turma', to='cadastros.Turma')),
                ('nome_disciplina', models.ForeignKey(db_column='nome_disciplina', on_delete=django.db.models.deletion.DO_NOTHING, related_name='arquivoNome_disciplina', to='cadastros.DisciplinaOfertada')),
            ],
            options={
                'db_table': 'ARQUIVO_QUESTAO',
            },
        ),
        migrations.CreateModel(
            name='ArquivoResposta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo', models.CharField(max_length=500, unique=True)),
                ('ano_ofertado', models.ForeignKey(db_column='ano_ofertado', on_delete=django.db.models.deletion.DO_NOTHING, related_name='arquivorAno_ofertado', to='cadastros.DisciplinaOfertada')),
                ('id_turma', models.ForeignKey(db_column='id_turma', on_delete=django.db.models.deletion.DO_NOTHING, related_name='arquivorId_turma', to='cadastros.Turma')),
                ('nome_disciplina', models.ForeignKey(db_column='nome_disciplina', on_delete=django.db.models.deletion.DO_NOTHING, related_name='arquivorNome_disciplina', to='cadastros.DisciplinaOfertada')),
            ],
            options={
                'db_table': 'ARQUIVO_RESPOSTA',
            },
        ),
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(unique=True)),
                ('data_limite_entrega', models.DateField()),
                ('descricao', models.TextField(blank=True, null=True)),
                ('data', models.DateField()),
                ('ano_ofertado', models.ForeignKey(db_column='ano_ofertado', on_delete=django.db.models.deletion.DO_NOTHING, related_name='questãoAno_ofertado', to='cadastros.DisciplinaOfertada')),
                ('id_turma', models.ForeignKey(db_column='id_turma', on_delete=django.db.models.deletion.DO_NOTHING, related_name='questaoId_turma', to='cadastros.Turma')),
                ('nome_disciplina', models.ForeignKey(db_column='nome_disciplina', on_delete=django.db.models.deletion.DO_NOTHING, related_name='questaoNome_disciplina', to='cadastros.DisciplinaOfertada')),
                ('semestre_ofertado', models.ForeignKey(db_column='semestre_ofertado', on_delete=django.db.models.deletion.DO_NOTHING, related_name='questaoSemestre_ofertado', to='cadastros.DisciplinaOfertada')),
            ],
            options={
                'db_table': 'QUESTAO',
            },
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ra_aluno', models.IntegerField(unique=True)),
                ('data_avaliacao', models.DateField()),
                ('nota', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('avaliacao', models.TextField()),
                ('descricao', models.TextField()),
                ('data_de_envio', models.DateField()),
                ('ano_ofertado', models.ForeignKey(db_column='ano_ofertado', on_delete=django.db.models.deletion.DO_NOTHING, related_name='respostaAno_ofertado', to='cadastros.DisciplinaOfertada')),
                ('id_turma', models.ForeignKey(db_column='id_turma', on_delete=django.db.models.deletion.DO_NOTHING, related_name='respostaId_turma', to='cadastros.Turma')),
                ('nome_disciplina', models.ForeignKey(db_column='nome_disciplina', on_delete=django.db.models.deletion.DO_NOTHING, related_name='respostaNome_disciplina', to='cadastros.DisciplinaOfertada')),
                ('numero_questao', models.ForeignKey(db_column='numero_questao', on_delete=django.db.models.deletion.DO_NOTHING, related_name='respostaArquivo_questao', to='questionario.Questao')),
                ('semestre_ofertado', models.ForeignKey(db_column='semestre_ofertado', on_delete=django.db.models.deletion.DO_NOTHING, related_name='respostaSemestre_ofertado', to='cadastros.DisciplinaOfertada')),
            ],
            options={
                'db_table': 'RESPOSTA',
            },
        ),
        migrations.AddField(
            model_name='arquivoresposta',
            name='numero_questao',
            field=models.ForeignKey(db_column='numero_questao', on_delete=django.db.models.deletion.DO_NOTHING, related_name='arquivorNumero_questao', to='questionario.Questao'),
        ),
        migrations.AddField(
            model_name='arquivoresposta',
            name='ra_aluno',
            field=models.ForeignKey(db_column='ra_aluno', on_delete=django.db.models.deletion.DO_NOTHING, related_name='arquivorRa_aluno', to='questionario.Resposta'),
        ),
        migrations.AddField(
            model_name='arquivoresposta',
            name='semestre_ofertado',
            field=models.ForeignKey(db_column='semestre_ofertado', on_delete=django.db.models.deletion.DO_NOTHING, related_name='arquivorSemestre_ofertado', to='cadastros.DisciplinaOfertada'),
        ),
        migrations.AddField(
            model_name='arquivoquestao',
            name='numero_questao',
            field=models.ForeignKey(db_column='numero_questao', on_delete=django.db.models.deletion.DO_NOTHING, related_name='arquivoNumero_questao', to='questionario.Questao'),
        ),
        migrations.AddField(
            model_name='arquivoquestao',
            name='semestre_ofertado',
            field=models.ForeignKey(db_column='semestre_ofertado', on_delete=django.db.models.deletion.DO_NOTHING, related_name='arquivoSemestre_ofertado', to='cadastros.DisciplinaOfertada'),
        ),
    ]
