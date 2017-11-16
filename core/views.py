from django.shortcuts import render, redirect
from cadastros.forms import AlunoForm, MatriculaForm
from django.contrib.auth.decorators import login_required, user_passes_test

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

def login(request):
    return render(request, "login.html")

def checa_aluno(usuario):
    return usuario.perfil == "A"

def checa_professor(usuario):
    return usuario.perfil == "P"

@login_required(login_url="/login")
@user_passes_test(checa_aluno)
def pagina_aluno(request):
    return render(request, "pagina_aluno.html")

@login_required(login_url="/login")
@user_passes_test(checa_professor)
def pagina_professor(request):
    return render(request, "pagina_professor.html")

def contato(request):
    return render(request, "contato.html")

def matricula1(request):
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

    return render(request, "matricula1.html", context)

def matricula2(request):
    if request.POST:
        form = MatriculaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MatriculaForm()

    context = {
        'form' : form
    }

    return render(request, "matricula2.html", context)
