from django.shortcuts import render
from core.models import curso

# Create your views here.

def index(request):
    contexto = {'id':curso.nome}
    return render(request, "index.html", contexto)
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