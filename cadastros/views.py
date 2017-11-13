from django.shortcuts import render, redirect
from .forms import *

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

def cadastro_curso(request):
    if request.POST:
        form_c = CursoForm(request.POST)
        if form_c.is_valid():
            form_c.save()
            return redirect('/cadastro_gradeCurricular')
    else:
        form_c = CursoForm()
    context = {
        'form_c' : form_c,
    }
    return render(request, "cadastro_curso.html", context)

def cadastro_gradeCurricular(request):
    if request.POST:
        form_gc = GradeCurricularForm(request.POST)
        if form_gc.is_valid():
            form_gc.save()
    else:
        form_gc = GradeCurricularForm()
    context = {
        'form_gc' : form_gc
    }
    return render(request, "cadastro_gradeCurricular.html", context)

def cadastro_periodo(request):
    if request.POST:
        form_p = PeriodoForm(request.POST)
        if form_p.is_valid():
            form_p.save()
    else:
        form_p = PeriodoForm()
    context = {
        'form_p' : form_p
    }
    return render(request, 'cadastro_periodo.html', context)

def cadastro_turma(request):
    if request.POST:
        form = TurmaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TurmaForm()
    context = {
        'form' : form
    }
    return render(request, "cadastro_turma.html", context)

def cadastro_disciplina(request):
    if request.POST:
        form_d = DisciplinaForm(request.POST)
        if form_d.is_valid():
            form_d.save()
    else:
        form_d = DisciplinaForm()
    context = {
        'disciplina' : form_d,
    }
    return render(request, "cadastro_disciplina.html", context)

def cadastro_disciplinaOfertada(request):
    if request.POST:
        form = DisciplinaOfertadaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = DisciplinaOfertadaForm()

    context = {
        'disciplina_o' : form
    }

    return render(request, "cadastro_disciplinaOfertada.html", context)