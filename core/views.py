from django.shortcuts import render, redirect
from cadastros.forms import AlunoForm, MatriculaForm
from django.contrib.auth.decorators import login_required, user_passes_test
from cadastros.models import Aluno, DisciplinaOfertada, Disciplina

# Create your views here.
def home(request):
    return render(request, "index.html")

def cursos(request):
    return render(request, "cursos.html")

def noticias(request):
    return render(request, "noticias.html")

def grade(request):
    return render(request, "grade-curricular.html")

def detalhes(request):
    return render(request, "detalhes.html")

def checa_aluno(usuario):
    return usuario.perfil == "A"

def checa_professor(usuario):
    return usuario.perfil == "P"

@login_required(login_url="/login")
@user_passes_test(checa_aluno)
def pagina_aluno(request):
    aluno = Aluno.objects.get(id=request.user.id)
    disciplinas = DisciplinaOfertada.objects.all()
    context = {
        'curso' : aluno.sigla_curso.nome,
        'disciplinasOfertadas' : disciplinas
    }
    return render(request, "pagina_aluno.html", context)

@login_required(login_url="/login")
@user_passes_test(checa_professor)
def pagina_professor(request):
    return render(request, "pagina_professor.html")

def contato(request):
    return render(request, "contato.html")

def matricula(request):
    if request.POST:
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = AlunoForm()
        

    context = {
        'form' : form
    }
    #django-widget-tweaks

    return render(request, "matricula.html", context)

def matricula_disciplina(request):
    if request.POST:
        form = MatriculaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MatriculaForm()

    context = {
        'form' : form
    }

    return render(request, "matricula_disciplina.html", context)

def tec_web(request):
    disciplina = Disciplina.objects.get(nome="Tecweb")
    context = {
        'disciplina' : disciplina
    }

    return render(request, "tec-web.html", context)

def lp_ii(request):
    disciplina = Disciplina.objects.get(nome="LPII")
    context = {
        'disciplina' : disciplina
    }

    return render(request, "tec-web.html", context)