from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from core.forms import contato_forms, questao_arquivo
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):
    def __unicode__(self):
    	return unicode(self.user)	
    return render(request, "index.html")
def Contato(request):
    def __unicode__(self):
    	return unicode(self.user)
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
    def __unicode__(self):
    	return unicode(self.user)
    return render(request, "cursos.html")
def detalhes(request):
    def __unicode__(self):
    	return unicode(self.user)
    return render(request, "detalhes.html")
def EsqueciSenha(request):
    def __unicode__(self):
    	return unicode(self.user)
    return render(request, "EsqueciSenha.html")
def noticias(request):
    def __unicode__(self):
    	return unicode(self.user)
    return render(request, "noticias.html")
def NovaDisciplina(request):
    def __unicode__(self):
    	return unicode(self.user)
    return render(request, "NovaDisciplina.html")
def NovoCadastro(request):
    def __unicode__(self):
    	return unicode(self.user)
    return render(request, "NovoCadastro.html")
def disciplinas(request):
    def __unicode__(self):
    	return unicode(self.user)
    return render(request, "disciplinas.html")

def login(request):
    def __unicode__(self):
    	return unicode(self.user)
    return render(request, "login.html")

def checa_aluno(user):
     return user.perfil == 'A'

def checa_professor(user):
     return user.perfil == 'P'

def questao_forms(request):
    def __unicode__(self):
    	return unicode(self.user)
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
