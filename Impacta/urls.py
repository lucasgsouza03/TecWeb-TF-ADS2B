"""Impacta URL Configuration

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
from core.views import *
from django.contrib.auth.views import login,logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login,{'template_name':'login.html'}, name='login'),
    url(r'^$', index),
    url(r'^index/', index, name='home'),
    url(r'^contato/', Contato, name='contato'),
    url(r'^cursos/', cursos, name='cursos'),
    url(r'^detalhes/', detalhes, name='detalhes'),
    url(r'^disciplinas/', disciplinas, name='disciplinas'),
    url(r'^EsqueciSenha/', EsqueciSenha, name='senha'),
    url(r'^noticias/', noticias, name='noticias'),
    url(r'^NovaDisciplina/', NovaDisciplina, name='novadisciplina'),
    url(r'^NovoCadastro/', NovoCadastro, name='novocadastro'),
    url(r'^logout/', logout, name='logout'),
    url(r'^aluno/$', aluno, name='aluno'),
    url(r'^professor/$', professor, name='professor'),
    url(r'^professor/questao', questao_forms, name='questao_forms'),
]

#if settings.DEBUG:
#   urlpatterns += static(settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT)