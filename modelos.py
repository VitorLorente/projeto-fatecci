# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Aluno(models.Model):
    ra = models.IntegerField(unique=True)
    nome = models.CharField(max_length=120)
    email = models.CharField(max_length=80)
    celular = models.CharField(max_length=11, blank=True, null=True)
    sigla_curso = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'ALUNO'


class ArquivoQuestao(models.Model):
    nome_disciplina = models.ForeignKey('DisciplinaOfertada', models.DO_NOTHING, db_column='nome_disciplina')
    ano_ofertado = models.ForeignKey('DisciplinaOfertada', models.DO_NOTHING, db_column='ano_ofertado')
    semestre_ofertado = models.ForeignKey('DisciplinaOfertada', models.DO_NOTHING, db_column='semestre_ofertado')
    id_turma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='id_turma')
    numero_questao = models.ForeignKey('Questao', models.DO_NOTHING, db_column='numero_questao')
    arquivo = models.CharField(unique=True, max_length=500)

    class Meta:
        managed = False
        db_table = 'ARQUIVO_QUESTAO'


class ArquivoResposta(models.Model):
    nome_disciplina = models.ForeignKey('DisciplinaOfertada', models.DO_NOTHING, db_column='nome_disciplina')
    ano_ofertado = models.ForeignKey('DisciplinaOfertada', models.DO_NOTHING, db_column='ano_ofertado')
    semestre_ofertado = models.ForeignKey('DisciplinaOfertada', models.DO_NOTHING, db_column='semestre_ofertado')
    id_turma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='id_turma')
    numero_questao = models.ForeignKey('Questao', models.DO_NOTHING, db_column='numero_questao')
    ra_aluno = models.ForeignKey('Resposta', models.DO_NOTHING, db_column='ra_aluno')
    arquivo = models.CharField(unique=True, max_length=500)

    class Meta:
        managed = False
        db_table = 'ARQUIVO_RESPOSTA'


class Curso(models.Model):
    sigla = models.CharField(unique=True, max_length=5)
    nome = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'CURSO'


class CursoTurma(models.Model):
    sigla_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='sigla_curso')
    nome_disciplina = models.ForeignKey('DisciplinaOfertada', models.DO_NOTHING, db_column='nome_disciplina')
    ano_ofertado = models.ForeignKey('DisciplinaOfertada', models.DO_NOTHING, db_column='ano_ofertado')
    semestre_ofertado = models.ForeignKey('DisciplinaOfertada', models.DO_NOTHING, db_column='semestre_ofertado')
    id_turma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='id_turma', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CURSO_TURMA'


class Disciplina(models.Model):
    nome = models.CharField(unique=True, max_length=240)
    carga_horaria = models.SmallIntegerField()
    teoria = models.DecimalField(max_digits=3, decimal_places=0)
    pratica = models.DecimalField(max_digits=3, decimal_places=0)
    ementa = models.TextField()  # This field type is a guess.
    competencias = models.TextField()  # This field type is a guess.
    habilidades = models.TextField(blank=True, null=True)  # This field type is a guess.
    conteudo = models.TextField()  # This field type is a guess.
    bibliografia_basica = models.TextField(blank=True, null=True)  # This field type is a guess.
    bibliografia_complementar = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'DISCIPLINA'


class DisciplinaOfertada(models.Model):
    nome_disciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='nome_disciplina', unique=True)
    ano = models.SmallIntegerField(unique=True)
    semestre = models.CharField(unique=True, max_length=1)

    class Meta:
        managed = False
        db_table = 'DISCIPLINA_OFERTADA'


class GradeCurricular(models.Model):
    sigla_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='sigla_curso')
    ano = models.SmallIntegerField(unique=True)
    semestre = models.CharField(unique=True, max_length=1)

    class Meta:
        managed = False
        db_table = 'GRADE_CURRICULAR'


class Matricula(models.Model):
    ra_aluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='ra_aluno')
    nome_disciplina = models.ForeignKey(DisciplinaOfertada, models.DO_NOTHING, db_column='nome_disciplina')
    ano_ofertado = models.ForeignKey(DisciplinaOfertada, models.DO_NOTHING, db_column='ano_ofertado')
    semestre_ofertado = models.ForeignKey(DisciplinaOfertada, models.DO_NOTHING, db_column='semestre_ofertado')
    id_turma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='id_turma')

    class Meta:
        managed = False
        db_table = 'MATRICULA'


class Periodo(models.Model):
    sigla_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='sigla_curso', blank=True, null=True)
    ano_grade = models.ForeignKey(GradeCurricular, models.DO_NOTHING, db_column='ano_grade')
    semestre_grade = models.ForeignKey(GradeCurricular, models.DO_NOTHING, db_column='semestre_grade')
    numero = models.SmallIntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'PERIODO'


class PeriodoDisciplina(models.Model):
    sigla_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='sigla_curso', blank=True, null=True)
    ano_grade = models.ForeignKey(GradeCurricular, models.DO_NOTHING, db_column='ano_grade')
    semestre_grade = models.ForeignKey(GradeCurricular, models.DO_NOTHING, db_column='semestre_grade')
    numero_periodo = models.ForeignKey(Periodo, models.DO_NOTHING, db_column='numero_periodo')
    nome_disciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='nome_disciplina')

    class Meta:
        managed = False
        db_table = 'PERIODO_DISCIPLINA'


class Professor(models.Model):
    ra = models.IntegerField(unique=True)
    apelido = models.CharField(unique=True, max_length=30)
    nome = models.CharField(max_length=120)
    email = models.CharField(max_length=80)
    celular = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PROFESSOR'


class Questao(models.Model):
    nome_disciplina = models.ForeignKey(DisciplinaOfertada, models.DO_NOTHING, db_column='nome_disciplina')
    ano_ofertado = models.ForeignKey(DisciplinaOfertada, models.DO_NOTHING, db_column='ano_ofertado')
    semestre_ofertado = models.ForeignKey(DisciplinaOfertada, models.DO_NOTHING, db_column='semestre_ofertado')
    id_turma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='id_turma')
    numero = models.IntegerField(unique=True)
    data_limite_entrega = models.DateField()
    descricao = models.TextField(blank=True, null=True)  # This field type is a guess.
    data = models.DateField()

    class Meta:
        managed = False
        db_table = 'QUESTAO'


class Resposta(models.Model):
    nome_disciplina = models.ForeignKey(DisciplinaOfertada, models.DO_NOTHING, db_column='nome_disciplina')
    ano_ofertado = models.ForeignKey(DisciplinaOfertada, models.DO_NOTHING, db_column='ano_ofertado')
    semestre_ofertado = models.ForeignKey(DisciplinaOfertada, models.DO_NOTHING, db_column='semestre_ofertado')
    id_turma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='id_turma')
    numero_questao = models.ForeignKey(Questao, models.DO_NOTHING, db_column='numero_questao')
    ra_aluno = models.IntegerField(unique=True)
    data_avaliacao = models.DateField()
    nota = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    avaliacao = models.TextField()  # This field type is a guess.
    descricao = models.TextField()  # This field type is a guess.
    data_de_envio = models.DateField()

    class Meta:
        managed = False
        db_table = 'RESPOSTA'


class Turma(models.Model):
    nome_disciplina = models.ForeignKey(DisciplinaOfertada, models.DO_NOTHING, db_column='nome_disciplina')
    ano_ofertado = models.ForeignKey(DisciplinaOfertada, models.DO_NOTHING, db_column='ano_ofertado')
    semestre_ofertado = models.ForeignKey(DisciplinaOfertada, models.DO_NOTHING, db_column='semestre_ofertado')
    id_turma = models.CharField(unique=True, max_length=1)
    ra_professor = models.ForeignKey(Professor, models.DO_NOTHING, db_column='ra_professor')

    class Meta:
        managed = False
        db_table = 'TURMA'
