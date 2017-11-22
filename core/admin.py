from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import Curso, Aluno, Professor
from django import forms

class NovoAlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ('ra','email', 'nome','curso')
        def save(self, commit=True):
            user = super(NovoAlunoForm, self).save(commit=False)
            user.set_password('123@mudar')
            user.perfil = 'A'
            if commit:
                user.save()
            return user

class AlterarAlunoForm(forms.ModelForm):
    class Meta:
            model = Aluno
            fields = ('email', 'nome', 'curso')

class AlunoAdmin(UserAdmin):
    form = AlterarAlunoForm
    add_form = NovoAlunoForm
    list_display = ('ra', 'email', 'nome', 'curso')
    list_filter = ('perfil',)
    fieldsets = ( (None, {'fields': ('ra', 'email', 'nome', 'curso')}),)
    add_fieldsets = (
        (None, { 
            'fields': ('ra', 'email', 'nome', 'curso')
            }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'carga_horaria')
    list_filter = ('tipo',)

class NovoProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ('nome', 'ra', 'email', 'apelido', 'celular')
    def save(self, commit=True):
        user = super(NovoProfessorForm, self).save(commit=False)
        user.set_password('123@mudar')
        user.perfil = 'P'
        if commit:
            user.save()
        return user

class AlterarProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ('nome', 'ra', 'email', 'apelido', 'celular')

class ProfessorAdmin(UserAdmin):
    form = AlterarProfessorForm
    add_form = NovoProfessorForm
    list_display = ('nome', 'ra', 'email', 'apelido', 'celular')
    list_filter = ('perfil',)
    fieldsets = ( (None, {'fields': ('nome', 'ra', 'email', 'apelido', 'celular')}),)
    add_fieldsets = (
        (None, { 
            'fields': ('nome', 'ra', 'email', 'apelido', 'celular')
            }),
    )
    search_fields = ('apelido',)
    ordering = ('apelido',)
    filter_horizontal = ()

# Register your models here.
admin.site.register(Aluno,AlunoAdmin)
admin.site.register(Curso,CursoAdmin)
admin.site.register(Professor,ProfessorAdmin)
