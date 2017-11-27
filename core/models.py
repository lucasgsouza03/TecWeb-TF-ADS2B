from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UsuarioManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, ra, password, **extra_fields):
        if not ra:
            raise ValueError('RA precisa ser preenchido')
        user = self.model(ra=ra, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, ra, password=None, **extra_fields):
        return self._create_user(ra, password, **extra_fields)

    def create_superuser(self, ra, password, **extra_fields):
        return self._create_user(ra, password, **extra_fields)


class Usuario(AbstractBaseUser):
    nome = models.CharField(max_length=100)
    ra = models.IntegerField(unique=True)   
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=150)
    perfil = models.CharField(max_length=1, default='C')
    ativo = models.BooleanField(default=True)

    USERNAME_FIELD = 'ra' 
    REQUIRED_FIELDS = ['nome'] 

    objects = UsuarioManager()

    @property
    def is_staff(self):
        return self.perfil == 'C'
    
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True

    def get_short_name(self):
        return self.nome
    def get_full_name(self):
        return self.nome

    def __unicode__(self):
        return self.nome

class Curso(models.Model):
    sigla = models.CharField(max_length=5)
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50,blank=True)
    carga_horaria = models.IntegerField(default=1000)
    ativo = models.BooleanField(default=True)

    descricao = models.TextField(blank=True)
    
    class Meta:
        db_table="curso"
    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome
    
class Aluno(Usuario):

    curso = models.ForeignKey(
        Curso
    )    

class Professor(Usuario):
    apelido = models.CharField(max_length=50)
    celular = models.CharField(max_length=11)

class GradeCurricular(models.Model):
    ano = models.SmallIntegerField(max_length=4)
    semestre = models.CharField(max_length=1)
    curso = models.ForeignKey(

        Curso

    ) 

   
    def __str__(self):
        return "{}".format(self.ano)

        
class Disciplina(models.Model):
    nome = models.CharField(max_length=240)
    carga_horaria = models.IntegerField(default=80)
    teoria = models.DecimalField(max_digits=3, decimal_places=0)
    pratica = models.DecimalField(max_digits=3, decimal_places=0)
    ementa = models.TextField()
    competencias = models.TextField()
    habilidades = models.TextField()
    conteudo = models.TextField()
    bibliografia_basica = models.TextField()
    bibliografia_complementar = models.TextField()
   
    def __str__(self):
        return self.nome

class Periodo(models.Model):
    numero = models.SmallIntegerField(unique=True)
    gradecurricular = models.ForeignKey(

        GradeCurricular

    )
    
    curso = models.ForeignKey(

        Curso
    )
    
  
    def __str__(self):
        return "{}".format(self.numero)

class PeriodoDisciplina(models.Model):
    Periodo = models.ForeignKey(

        Periodo

    )
    Disciplina = models.ForeignKey(

        Disciplina

    )

    def __str__(self):
        return "{}".format(self.Periodo, self.Disciplina)
    
class DisciplinaOfertada(models.Model):
    ano = models.SmallIntegerField(max_length=4)
    semestre = models.CharField(max_length=1)
    disciplina = models.ForeignKey(

        Disciplina

    )
    
    def __str__(self):
        return "{}".format(self.ano)

class Turma(models.Model):
    turma = models.CharField(max_length=100, unique=True)
    turno = models.CharField(max_length=15)
    ano = models.SmallIntegerField()
    semestre = models.CharField(max_length=1)
    disciplinaofertada = models.ForeignKey(

        DisciplinaOfertada

    )
    professor = models.ForeignKey(

        Professor

    )

    def __str__(self):
        return self.turma

class Matricula(models.Model):
    aluno = models.ForeignKey(

        Aluno

    )
    turma = models.ForeignKey(

        Turma

    )

    def __str__(self):
        return "{}".format(self.aluno, self.turma)

class CursoTurma(models.Model):
    curso = models.ForeignKey(

        Curso

    )
    turma = models.ForeignKey(

        Turma

    ) 

    def __str__(self):
        return "{}".format(self.curso, self.turma)
 

class questao(models.Model):

    disciplina = models.CharField(max_length=240)
    ano_ofertado = models.SmallIntegerField()
    semestre_ofertado = models.CharField(max_length=1)
    id_turma = models.CharField(max_length=1)
    numero = models.IntegerField()
    data_limite_entrega = models.DateField()
    descricao = models.TextField()
    data = models.DateField()
    turma = models.ForeignKey(

        Turma

    )

    def __str__(self):
        return "{}".format(self.numero)

class ArquivoQuestao(models.Model):
    arquivo = models.CharField(max_length=500)
    questao = models.ForeignKey(

        questao

      )

    def __str__(self):
        return self.arquivo