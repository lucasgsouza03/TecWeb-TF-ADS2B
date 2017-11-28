from django import forms
from django.core.mail import send_mail
from Impacta.settings import EMAIL_HOST_USER
from core.models import questao, ArquivoQuestao


class contato_forms(forms.Form):
    nome = forms.CharField()
    email = forms.EmailField()
    assunto = forms.CharField()
    mensagem = forms.CharField()

    def envia_email(self, assunto, mensagem, email):
        email = [email]
        send_mail(assunto, mensagem, EMAIL_HOST_USER, email, fail_silently=True)


class questao_arquivo(forms.ModelForm):
    class Meta:
        model = ArquivoQuestao
        fields = "__all__"
