from django.shortcuts import render

# Create your views here.
def cadastro_aluno(request):
    return render(request, "cadastro_aluno.html")