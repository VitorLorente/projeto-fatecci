"""projeto_fatecci URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from cadastros.views import *
from core.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cadastro_aluno$', cadastro_aluno, name='cadastro_aluno'),
    url(r'^cadastro_professor$', cadastro_professor, name='cadastro_professor'),
    url(r'^cadastro_curso$', cadastro_curso, name='cadastro_curso'),
    url(r'^cadastro_gradeCurricular$', cadastro_gradeCurricular, name='cadastro_gradeCurricular'),
    url(r'^cadastro_periodo$', cadastro_periodo, name='cadastro_periodo'),
    url(r'^cadastro_turma$', cadastro_turma, name='cadastro_turma'),
    url(r'^cadastro_disciplina$', cadastro_disciplina, name='cadastro_disciplina'),
    url(r'^cadastro_disciplinaOfertada$', cadastro_disciplinaOfertada, name='cadastro_disciplinaOfertada'),
    url(r'^cursos$', cursos, name='cursos'),
    url(r'^noticias$', noticias, name='noticias'),
    url(r'^grade_curricular$', grade, name='grade'),
    url(r'^detalhes$', detalhes, name='detalhes'),
    url(r'^login$', login, name='login'),
    url(r'^matricula1$', matricula1, name='matricula1'),
    url(r'^matricula2$', matricula2, name='matricula2'),
    url(r'^', home, name='home')
]
