from django.shortcuts import render, redirect
from .forms import *
from core.views import checa_aluno, checa_professor
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required(login_url="/login")
@user_passes_test(checa_professor)
def cadastro_avaliacao(request):
    if request.POST:
        form = QuestaoForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/cadastro_avaliacao2')

    else:
        form = QuestaoForm()        

    context = {
        'form' : form
    }

    return render(request, "cadastro_avaliacao.html", context)

@login_required(login_url="/login")
@user_passes_test(checa_professor)
def cadastro_avaliacao2(request):
    if request.POST:
        form = ArquivoQuestaoForm(request.POST, request.FILE)
        
        if form.is_valid():
            form.save()
    else:
        form = ArquivoQuestaoForm()
        

    context = {
        'form' : form
    }

    return render(request, "cadastro_avaliacao2.html", context)

@login_required(login_url="/login")
@user_passes_test(checa_aluno)
def cadastro_resposta(request):
    if request.POST:
        form = RespostaForm(request.POST)
        
        if form.is_valid():
            form.save()
            redirect('/cadastro_resposta2.html')
    else:
        form = RespostaForm()
        

    context = {
        'form' : form
    }

    return render(request, "cadastro_resposta.html", context)

@login_required(login_url="/login")
@user_passes_test(checa_aluno)
def cadastro_resposta2(request):
    if request.POST:
        form = ArquivoRespostaForm(request.POST, request.FILE)
        
        if form.is_valid():
            form.save()
    else:
        form = ArquivoRespostaForm()
        

    context = {
        'form' : form
    }

    return render(request, "cadastro_resposta2.html", context)