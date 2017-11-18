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
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^admin', admin.site.urls),
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
    url(r'^login$', login, {"template_name": "login.html"}, name='login'),
    url(r'^logout$', logout, {"template_name": "logout.html"}, name='logout'),
    url(r'^matricula$', matricula, name='matricula'),
    url(r'^matricula_disciplina$', matricula_disciplina, name='matricula_disciplina'),
    url(r'^tec-web$', tec_web, name="tec-web"),
    url(r'^lp-ii$', lp_ii, name="lp-ii"),
    url(r'^pagina_aluno$', pagina_aluno, name='pagina_aluno'),
    url(r'^pagina_professor$', pagina_professor, name='pagina_professor'),
    url(r'^contato$', contato, name='contato'),
    url(r'^', home, name='home')
]
