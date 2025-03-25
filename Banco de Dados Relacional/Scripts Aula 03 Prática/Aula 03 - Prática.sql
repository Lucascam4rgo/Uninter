create database aulapratica;
use aulapratica;

create table produto (
id int not null,
descricao varchar(100),
preco decimal(8, 2)
);

insert into produto values (1, "Smartphone xpto" , 1500.99);

insert into produto values (2, "Notebook i7 8gb ram" , 2500);

select * from produto;

select * from produto order by preco desc; -- asc/desc

drop table produto;

show tables;

create table aluno (
	id int,
    nome varchar(100) not null, 
    genero char(01),
    nascimento date,
    estadoCivil char(01) check (estadoCivil in ('C', 'S', 'V', 'O')),
    salario decimal(10, 2) unsigned default 0,
    email varchar(120) unique
);

insert into aluno values (1, 'Helena Magalhães', 'F', '2000-01-01', 'C', 12500.99, 'helena.magalhaes@email.com'),
                         (2, 'Nicolas Oliveira', 'M', '2002-12-10', 'S', 8500, 'nicolas.oliveira@email.com'),
                         (3, 'Ana Rosa Silva', 'F', '1996-12-31', 'S', 8500, 'ana.rosa@email.com'),
                         (4, 'Tales Heitor Souza', 'M', '2000-10-01', 'O', 7689, 'tales.heitor@email.com'),
                         (5, 'Bia Meireles', 'F', '2002-03-14', 'O', 9450, 'bia.meireles@email.com'),
                         (6, 'Pedro Filho', 'M', null, 'V', 6800, 'pedro.filho@email.com'),
                         (7, 'Helena Soares', 'F', '1994-08-10', 'S', 8600, 'helena.soares@email.com');
                         

select * from aluno;

insert into aluno (id, genero, nascimento, estadoCivil, email) values (8, 'F', '2000-01-01', 'X', 'helena.magalhaes@email.com');

create table estado (
	id int not null primary key auto_increment,
    nome varchar(100) not null
);

insert into estado (nome) values (2, "Mato Grosso");

select * from estado;

create table cidade (
	id int not null primary key auto_increment,
    nome varchar(100) not null,
    idEstado int,
    constraint fkCidadeEstado foreign key (idEstado)
    references estado(id)
);

insert into cidade (nome, idEstado) values ("Salvador", 2);

select * from cidade;

insert into cidade (nome, idEstado) values ("São Caetano", 1);

alter table aluno
add telefone varchar(10);
select * from aluno;

alter table aluno
change telefone celular varchar(12);

alter table aluno
add ddd int zerofill after email;

describe aluno;

alter table aluno modify celular varchar(14);

alter table aluno rename to alunos;

alter table alunos add constraint pkAluno primary key(id);

describe alunos;

alter table alunos drop primary key;

select * from alunos;

