from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from core.forms import contato_forms, questao_arquivo, solicita_matricula
from core.models import Curso, Disciplina

# Create your views here.

def index(request):	
    return render(request, "index.html")
def Contato(request):
    if request.POST:
        form = contato_forms(request.POST)
        if form.is_valid():
            assunto = request.POST.get("assunto")
            mensagem = request.POST.get("mensagem")
            email = request.POST.get("email")
            form.envia_email(assunto, mensagem, email)
    else:
        form = contato_forms()
    contexto = {
                "form":form
	            }
    return render(request, "Contato.html", contexto)
def cursos(request):
    contexto = {
        "cursos":Curso.objects.all()
    }
    return render(request, "cursos.html", contexto)
def detalhes(request, sigla):
    if request.POST:
        form = solicita_matricula(request.POST)
        if form.is_valid():
            nome = request.POST.get("nome")
            email = request.POST.get("email")
            cel = request.POST.get("cel")
	    curs = sigla
            form.envia_email(nome, email, cel, curs)
    else:
        form = solicita_matricula()
	
    curso = Curso.objects.get(sigla=sigla)
    contexto = {
        "curso": curso,
	"form": form
    }
    return render(request, "detalhes.html", contexto)

def EsqueciSenha(request):
    return render(request, "EsqueciSenha.html")
def noticias(request):
    return render(request, "noticias.html")
def NovaDisciplina(request):
    return render(request, "NovaDisciplina.html")
def NovoCadastro(request):
    return render(request, "NovoCadastro.html")
def disciplinas(request):
    cursos = Disciplina.objects.all()
    contexto = { "cursos":cursos}
    return render(request, "disciplinas.html", contexto)

def login(request):
    return render(request, "login.html")

def checa_aluno(user):
     return user.perfil == 'A'

def checa_professor(user):
     return user.perfil == 'P'

def questao_forms(request):
    if request.POST:
        arq = questao_arquivo(request.POST, request.FILES)
        if arq.is_valid():
            arq.save()
    else:
        arq = questao_arquivo()
    contexto = {
                "arq":arq
	            }
    return render(request, "questao_form.html", contexto)

@login_required(login_url='/login')

@user_passes_test(checa_aluno, login_url='aluno.html', redirect_field_name=None)
def aluno(request):
    return render(request, "aluno.html")

@user_passes_test(checa_professor, login_url='/?error=acesso', redirect_field_name=None)

@login_required(login_url='/login')
def professor(request):
    contexto = {
        'disciplinas':[{'nome':'tec'},{'nome':'sql'},{'nome':'lp2'}]
    }
    return render(request, "professor.html", contexto)

