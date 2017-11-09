from django.shortcuts import render
from .forms import AlunoForm, ProfessorForm

# Create your views here.
def cadastro_aluno(request):
    
    if request.POST:
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AlunoForm()
    context = {
        'form' : form
    }

    return render(request, "cadastro_aluno.html", context)

def cadastro_professor(request):
    
    if request.POST:
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProfessorForm()
    context = {
        'form' : form
    }

    return render(request, "cadastro_professor.html", context)
