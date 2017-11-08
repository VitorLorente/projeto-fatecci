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