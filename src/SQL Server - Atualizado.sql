
create table Curso(
id int not null AUTO_INCREMENT
,sigla varchar(10) not null
,nome varchar(100) not null
,constraint pk_Curso primary key(id)
,constraint uq_Curso unique(sigla, nome)
);


create table GradeCurricular(
id int not null AUTO_INCREMENT
,id_curso int not null
,ano smallint not null
,semestre char(1) not null
,constraint pk_GradeCurricular primary key(id)
,constraint fk_GradeCurricular foreign key(id_curso) references Curso(id)
,constraint uq_GradeCurricular unique(ano, semestre)  
);


create table Periodo(
id int not null AUTO_INCREMENT
,id_curso int not null
,id_grade int not null
,numero int not null
,constraint pk_Periodo primary key(id)
,constraint fk_Periodo foreign key(id_curso) references Curso(id)
,constraint fk_Periodo2 foreign key(id_grade) references GradeCurricular(id)
,constraint uq_Periodo unique(numero)
);


create table Disciplina(
id int not null AUTO_INCREMENT
,nome varchar(240) not null
,carga_horaria tinyint not null
,teoria decimal(3) not null
,pratica decimal(3) not null
,ementa text not null
,competencias text not null
,habilidades text not null
,conteudo text not null
,bib_basica text not null
,bib_complementar text not null
,constraint pk_Disciplina primary key(id)
,constraint uq_Disciplina unique(nome)
);


create table Professor(
id int not null AUTO_INCREMENT
,ra int not null
,apelido varchar(30) not null
,nome varchar(120) not null
,email varchar(80) not null
,celular char(11) not null
,constraint pk_Professor primary key(id)
,constraint uq_Professor unique(ra, apelido)
);


create table Aluno(
id int not null AUTO_INCREMENT
,id_curso int not null
,ra int not null
,nome varchar(120) not null
,email varchar(80) not null
,celular char(11) not null
,constraint pk_Aluno primary key(id)
,constraint fk_Aluno foreign key(id_curso) references Curso(id)
,constraint uq_Aluno unique(ra)
);

create table Disciplina_Ofertada(
id int not null AUTO_INCREMENT
,id_disciplina int not null
,ano smallint not null
,semestre char(1) not null
,constraint pk_Disciplina_Ofertada primary key(id)
,constraint fk_Disciplina_Ofertada foreign key(id_Disciplina) references Disciplina(id)
,constraint uq_Disciplina_Ofertada unique(ano, semestre)
);


create table Turma(
id int not null AUTO_INCREMENT
,id_disciplina_ofertada int not null
,id_professor int not null
,turno varchar(15) not null
,ano smallint not null
,semestre char(1) not null
,constraint pk_Turma primary key(id)
,constraint fk_Turma foreign key(id_disciplina_ofertada) references Disciplina_Ofertada(id)
,constraint fk_turma2 foreign key(id_professor) references Professor(id)
);


create table Questao(
id int not null AUTO_INCREMENT
,id_disciplina_ofertada int not null
,id_turma int not null
,numero int not null
,dt_limite_entrega date not null
,descricao text not null
,data date not null
,constraint pk_Questao primary key(id)
,constraint fk_questao foreign key(id_turma) references Turma(id)
,constraint uq_Questao unique(numero)
);


create table Arquivo_Questao(
id int not null AUTO_INCREMENT
,id_questao int not null
,arquivo varchar(500) not null
,constraint pk_Arquivo_Questao primary key(id)
,constraint fk_Arquivo_Questao foreign key(id_questao) references Questao(id)
,constraint uq_Arquivo_Questao unique(arquivo)
);


create table Resposta(
id int not null AUTO_INCREMENT
,id_questao int not null
,id_aluno int not null
,dt_avaliacao date not null
,nota decimal(4,2) not null
,avaliacao text not null
,descricao text not null
,dt_envio date not null
,constraint pk_Resposta primary key(id)
,constraint fk_Resposta foreign key(id_questao) references Questao(id)
,constraint fk_Resposta2 foreign key(id_aluno) references Aluno(id)
);


create table Arquivo_Resposta(
id int not null AUTO_INCREMENT
,id_resposta int not null
,arquivo varchar(500) not null
,constraint pk_Arquivo_Resposta primary key(id)
,constraint fk_Arquivo_Resposta foreign key(id_resposta) references Resposta(id)
,constraint uq_Arquivo_Resposta unique(arquivo)
);


create table Periodo_Disciplina(
id_Periodo int not null
,id_Disciplina int not null
,constraint pk_Periodo_Disciplina primary key(id_Periodo, id_Disciplina)
,constraint fk_Periodo_Disciplina foreign key(id_Periodo) references Periodo(id)
,constraint fk_PeriodoDisciplina foreign key(id_Disciplina) references Disciplina(id)
);

create table Matricula(
id int not null AUTO_INCREMENT
,id_aluno int not null
,id_turma int not null
,constraint pk_Matricula primary key(id)
,constraint fk_Matricula foreign key(id_aluno) references Aluno(id)
,constraint fk_Matricula2 foreign key(id_turma) references Turma(id)
);

create table Curso_Turma(
id_Curso int not null
,id_Turma int not null
,constraint pk_Curso_Turma primary key(id_Curso, id_Turma)
,constraint fk_Curso_Turma foreign key(id_Curso) references Curso(id)
,constraint fk_CursoTruma foreign key(id_Turma) references Turma(id)
);

alter table Periodo drop foreign key fk_Periodo;

alter table Periodo drop column id_Curso;
