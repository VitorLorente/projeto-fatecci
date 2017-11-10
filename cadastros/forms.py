from django.forms import ModelForm
from .models import Aluno, Professor, Disciplina

class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'

class ProfessorForm(ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'

class DisciplinaForm(ModelForm):
    class Meta:
        model = Disciplina
        fields = '__all__'