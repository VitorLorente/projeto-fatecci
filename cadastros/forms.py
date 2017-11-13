from django.forms import ModelForm
from .models import *

class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'

class ProfessorForm(ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

class DisciplinaForm(ModelForm):
    class Meta:
        model = Disciplina
        fields = '__all__'

class TurmaForm(ModelForm):
    class Meta:
        model = Turma
        fields = '__all__'

class DisciplinaOfertadaForm(ModelForm):
    class Meta:
        model = DisciplinaOfertada
        fields = '__all__'

class GradeCurricularForm(ModelForm):
    class Meta:
        model = GradeCurricular
        fields = '__all__'

class PeriodoForm(ModelForm):
    class Meta:
        model = Periodo
        fields = '__all__'

class PeriodoDisciplinaForm(ModelForm):
    class Meta:
        model = PeriodoDisciplina 
        fields = '__all__'

class MatriculaForm(ModelForm):
    class Meta:
        model = Matricula
        fields = '__all__'
