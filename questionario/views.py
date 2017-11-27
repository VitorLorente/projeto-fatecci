from django.shortcuts import render, redirect
from .forms import *
from core.views import checa_aluno, checa_professor
from cadastros.models import Aluno
from django.contrib.auth.decorators import login_required, user_passes_test

def corrige_gabarito(gabarito, resposta):
    i = 0
    nota = 0
    while i < 10:
        if resposta[i] == gabarito[i]:
            nota += 1
        i+=1 
    return nota


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
        form = ArquivoQuestaoForm(request.POST, request.FILES)
        
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
            return redirect('/cadastro_resposta2')
    else:
        form = RespostaForm()
        

    context = {
        'form' : form
    }

    return render(request, "cadastro_resposta.html", context)

@login_required(login_url="/login")
@user_passes_test(checa_aluno)
def cadastro_resposta2(request):
    aluno = Aluno.objects.get(id=request.user.id)
    if request.POST:
        resposta = Resposta.objects.get(ra_aluno=aluno.ra, id_turma=request.POST.get('id_turma'))
        gab = ArquivoQuestao.objects.get(nome_disciplina=request.POST.get('nome_disciplina'), id_turma=request.POST.get('id_turma'))
        questao = ArquivoQuestao.objects.get(id_turma=request.POST.get('id_turma'), nome_disciplina=request.POST.get('nome_disciplina'))
        gabarito = gab.gabarito.split(",")
        lista_respostas = []
        #rquivo = request.FILES.name
        form = ArquivoRespostaForm(request.POST, request.FILES)
        file = request.FILES['arquivo']
        path = 'core/static/'
        path += file.name
        if form.is_valid():
            form.save()
            with open(path, 'r') as f:
                datas = str(f.read())

            dts = datas.split(",")
            for data in dts:
                lista_respostas.append(data)
        
        resposta.nota = float(corrige_gabarito(gabarito, lista_respostas))
        resposta.save()
    else:
        form = ArquivoRespostaForm()
    context = {
        'form' : form
    }

    return render(request, "cadastro_resposta2.html", context)