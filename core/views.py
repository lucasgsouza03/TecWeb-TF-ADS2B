from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

def index(request):
    return render(request, "index.html")
def Contato(request):
    return render(request, "Contato.html")
def cursos(request):
    return render(request, "cursos.html")
def detalhes(request):
    return render(request, "detalhes.html")
def EsqueciSenha(request):
    return render(request, "EsqueciSenha.html")
def noticias(request):
    return render(request, "noticias.html")
def NovaDisciplina(request):
    return render(request, "NovaDisciplina.html")
def NovoCadastro(request):
    return render(request, "NovoCadastro.html")
def disciplinas(request):
    return render(request, "disciplinas.html")

def login(request):
    return render(request, "login.html")

def checa_aluno(user):
     return user.perfil == 'A'

def checa_professor(user):
     return user.perfil == 'P'


@login_required(login_url='/login')
@user_passes_test(checa_aluno, login_url='aluno.html', redirect_field_name=None)
def aluno(request):
    return render(request, "aluno.html")

@user_passes_test(checa_professor, login_url='/?error=acesso', redirect_field_name=None)
@login_required(login_url='/login')
def professor(request):
    return render(request, "professor.html")
