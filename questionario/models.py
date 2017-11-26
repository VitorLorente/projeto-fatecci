from django.db import models
from cadastros.models import *

class Questao(models.Model):
    nome_disciplina = models.ForeignKey(DisciplinaOfertada, models.DO_NOTHING, db_column='nome_disciplina', related_name="questaoNome_disciplina")
    ano_ofertado = models.ForeignKey(DisciplinaOfertada, models.DO_NOTHING, db_column='ano_ofertado', related_name="questãoAno_ofertado")
    semestre_ofertado = models.ForeignKey(DisciplinaOfertada, models.DO_NOTHING, db_column='semestre_ofertado', related_name="questaoSemestre_ofertado")
    id_turma = models.ForeignKey(Turma, models.DO_NOTHING, db_column='id_turma', related_name="questaoId_turma")
    numero = models.IntegerField(unique=True)
    data_limite_entrega = models.DateField()
    descricao = models.TextField(blank=True, null=True)  # This field type is a guess.
    data = models.DateField()

    class Meta:
        db_table = 'QUESTAO'

    def __str__(self):
        return 'Turma: {} Prazo: {} Questão: {}' .format(self.nome_disciplina, self.data_limite_entrega, self.numero)

class ArquivoQuestao(models.Model):
    nome_disciplina = models.ForeignKey(DisciplinaOfertada, models.DO_NOTHING, db_column='nome_disciplina', related_name="arquivoNome_disciplina")
    ano_ofertado = models.ForeignKey(DisciplinaOfertada, models.DO_NOTHING, db_column='ano_ofertado', related_name="arquivoAno_ofertado")
    semestre_ofertado = models.ForeignKey(DisciplinaOfertada, models.DO_NOTHING, db_column='semestre_ofertado', related_name="arquivoSemestre_ofertado")
    id_turma = models.ForeignKey(Turma, models.DO_NOTHING, db_column='id_turma', related_name="arquivoId_turma")
    numero_questao = models.ForeignKey(Questao, models.DO_NOTHING, db_column='numero_questao', related_name="arquivoNumero_questao")
    arquivo = models.FileField()
    gabarito = models.CharField(max_length=20)

    class Meta:
        db_table = 'ARQUIVO_QUESTAO'

    def __str__(self):
        return '{} {} {} {}'.format(self.nome_disciplina, self.ano_ofertado, self.semestre_ofertado, self.id_turma)

class Resposta(models.Model):
    nome_disciplina = models.ForeignKey(DisciplinaOfertada, models.DO_NOTHING, db_column='nome_disciplina', related_name="respostaNome_disciplina")
    ano_ofertado = models.ForeignKey(DisciplinaOfertada, models.DO_NOTHING, db_column='ano_ofertado', related_name="respostaAno_ofertado")
    semestre_ofertado = models.ForeignKey(DisciplinaOfertada, models.DO_NOTHING, db_column='semestre_ofertado', related_name="respostaSemestre_ofertado")
    id_turma = models.ForeignKey(Turma, models.DO_NOTHING, db_column='id_turma', related_name="respostaId_turma")
    numero_questao = models.ForeignKey(Questao, models.DO_NOTHING, db_column='numero_questao', related_name="respostaArquivo_questao")
    ra_aluno = models.IntegerField(unique=True)
    data_avaliacao = models.DateField()
    nota = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    data_de_envio = models.DateField()

    class Meta:
        db_table = 'RESPOSTA'

    def __str__(self):
        return str(self.ra_aluno)

class ArquivoResposta(models.Model):
    nome_disciplina = models.ForeignKey(DisciplinaOfertada, models.DO_NOTHING, db_column='nome_disciplina', related_name="arquivorNome_disciplina")
    ano_ofertado = models.ForeignKey(DisciplinaOfertada, models.DO_NOTHING, db_column='ano_ofertado', related_name="arquivorAno_ofertado")
    semestre_ofertado = models.ForeignKey(DisciplinaOfertada, models.DO_NOTHING, db_column='semestre_ofertado', related_name="arquivorSemestre_ofertado")
    id_turma = models.ForeignKey(Turma, models.DO_NOTHING, db_column='id_turma', related_name="arquivorId_turma")
    numero_questao = models.ForeignKey(Questao, models.DO_NOTHING, db_column='numero_questao', related_name="arquivorNumero_questao")
    ra_aluno = models.ForeignKey(Resposta, models.DO_NOTHING, db_column='ra_aluno', related_name="arquivorRa_aluno")
    arquivo = models.FileField()

    class Meta:
        db_table = 'ARQUIVO_RESPOSTA'
