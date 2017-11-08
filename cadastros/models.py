from django.db import models

# Create your models here.
class Aluno(models.Model):
    ra = models.IntegerField(unique=True)
    nome = models.CharField(max_length=120)
    email = models.CharField(max_length=80)
    celular = models.CharField(max_length=11, blank=True, null=True)
    sigla_curso = models.CharField(max_length=2)

    class Meta:
        db_table = 'ALUNO'

class Professor(models.Model):
    ra = models.IntegerField(unique=True)
    apelido = models.CharField(unique=True, max_length=30)
    nome = models.CharField(max_length=120)
    email = models.CharField(max_length=80)
    celular = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        db_table = 'PROFESSOR'

class Disciplina(models.Model):
    nome = models.CharField(unique=True, max_length=240, db_column='nome_disciplina')
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
        db_table = 'DISCIPLINA'

class DisciplinaOfertada(models.Model):
    nome_disciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='nome_disciplina', unique=True)
    ano = models.SmallIntegerField(unique=True)
    semestre = models.CharField(unique=True, max_length=1)

    class Meta:
        db_table = 'DISCIPLINA_OFERTADA'

class Curso(models.Model):
    sigla = models.CharField(unique=True, max_length=5)
    nome = models.CharField(unique=True, max_length=50)

    class Meta:
        db_table = 'CURSO'

class GradeCurricular(models.Model):
    sigla_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='sigla_curso')
    ano = models.SmallIntegerField(unique=True)
    semestre = models.CharField(unique=True, max_length=1)

    class Meta:
        db_table = 'GRADE_CURRICULAR'

class Periodo(models.Model):
    sigla_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='sigla_curso', blank=True, null=True)
    ano_grade = models.ForeignKey(GradeCurricular, models.DO_NOTHING, db_column='ano_grade', related_name='ano_periodo')
    semestre_grade = models.ForeignKey(GradeCurricular, models.DO_NOTHING, db_column='semestre_grade', related_name='semestre_periodo')
    numero = models.SmallIntegerField(unique=True)

    class Meta:
        db_table = 'PERIODO'

class PeriodoDisciplina(models.Model):
    sigla_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='sigla_curso', blank=True, null=True)
    ano_grade = models.ForeignKey(GradeCurricular, models.DO_NOTHING, db_column='ano_grade', related_name='ano_periodo_disciplina')
    semestre_grade = models.ForeignKey(GradeCurricular, models.DO_NOTHING, db_column='semestre_grade', related_name='semestre_periodo_disciplina')
    numero_periodo = models.ForeignKey(Periodo, models.DO_NOTHING, db_column='numero_periodo')
    nome_disciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='nome_disciplina')

    class Meta:
        db_table = 'PERIODO_DISCIPLINA'

class Turma(models.Model):
    nome_disciplina = models.ForeignKey(DisciplinaOfertada, models.DO_NOTHING, db_column='nome_disciplina', related_name='nome_disciplina_turma')
    ano_ofertado = models.ForeignKey(DisciplinaOfertada, models.DO_NOTHING, db_column='ano_ofertado', related_name='ano_turma')
    semestre_ofertado = models.ForeignKey(DisciplinaOfertada, models.DO_NOTHING, db_column='semestre_ofertado', related_name='semestre_turma')
    id_turma = models.CharField(unique=True, max_length=1)
    ra_professor = models.ForeignKey(Professor, models.DO_NOTHING, db_column='ra_professor')

    class Meta:
        db_table = 'TURMA'

class Matricula(models.Model):
    ra_aluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='ra_aluno')
    nome_disciplina = models.ForeignKey(DisciplinaOfertada, models.DO_NOTHING, db_column='nome_disciplina', related_name='nome_disciplina_matricula')
    ano_ofertado = models.ForeignKey(DisciplinaOfertada, models.DO_NOTHING, db_column='ano_ofertado', related_name='ano_ofertado_matricula')
    semestre_ofertado = models.ForeignKey(DisciplinaOfertada, models.DO_NOTHING, db_column='semestre_ofertado', related_name='semestre_ofertado_matricula')
    id_turma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='id_turma')

    class Meta:
        db_table = 'MATRICULA'