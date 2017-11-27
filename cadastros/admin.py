from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import *

class CursoAdmin(admin.ModelAdmin):
    list_display = ["nome", "sigla"]

class ProfessorAdmin(UserAdmin):
    add_form = ProfessorForm
    #form = AlunoAlterarForm
    add_fieldsets = ((None, { "fields": ("ra", "nome", "email", "apelido")}),)
    fieldsets = ((None, { "fields": ("nome", "email", "apelido", "ativo")}),)
    list_display = ["ra","nome","email", "apelido"]
    filter_horizontal = []
    ordering = ["ra"]
    list_filter = ["apelido"]

class AlunoAdmin(UserAdmin):
    add_form = AlunoForm
    #form = AlunoAlterarForm
    add_fieldsets = ((None, { "fields": ("ra", "nome", "email", "curso")}),)
    fieldsets = ((None, { "fields": ("nome", "email", "curso", "ativo")}),)
    list_display = ["ra", "nome", "email"]
    filter_horizontal = []
    ordering = ["ra"]
    list_filter = ["nome", "ra"]

class MatriculaAdmin(admin.ModelAdmin):
    add_form = MatriculaForm
    add_fieldsets = ((None, { "fields": ("ra_aluno", "nome_disciplina", "ano_ofertado", "semestre_ofertado", "id_turma")}),)
    fieldsets = ((None, { "fields": ("nome_disciplina", "ano_ofertado", "semestre_ofertado", "id_turma")}),)
    list_display = ["ra_aluno", "nome_disciplina", "id_turma"]
    filter_horizontal = []
    ordering = ["id_turma"]
    list_filter = ["ra_aluno", "nome_disciplina", "ano_ofertado", "semestre_ofertado", "id_turma"]
    search_fields = ('semestre_ofertado', 'ano_ofertado')

class PeriodoDisciplinaAdmin(admin.ModelAdmin):
    list_display = ["sigla_curso", "ano_grade", "semestre_grade", "numero_periodo", "nome_disciplina"]

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ["nome", "carga_horaria"]

class DisciplinaOfertadaAdmin(admin.ModelAdmin):
    list_display = ["nome_disciplina", "ano", "semestre"]

class GradeCurricularAdmin(admin.ModelAdmin):
    list_display = ["sigla_curso", "ano", "semestre"]

class PeriodoAdmin(admin.ModelAdmin):
    list_display = ["sigla_curso", "ano_grade", "semestre_grade", "numero"]

class TurmaAdmin(admin.ModelAdmin):
    list_display = ["nome_disciplina", "semestre_ofertado", "id_turma", "ra_professor"]


admin.site.register(Curso, CursoAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(DisciplinaOfertada, DisciplinaOfertadaAdmin)
admin.site.register(GradeCurricular, GradeCurricularAdmin)
admin.site.register(Periodo, PeriodoAdmin)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Matricula, MatriculaAdmin)
admin.site.register(PeriodoDisciplina, PeriodoDisciplinaAdmin)