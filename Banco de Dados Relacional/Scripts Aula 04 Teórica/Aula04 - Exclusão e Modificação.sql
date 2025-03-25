-- Inserir os registros  na tabela cidade
use aula;

create table cidade4 (
	id int,
    nome varchar(100) not null,
    uf char(02), 
    constraint pkCidade primary key (id)
);

insert into cidade4 values (1, 'Curitiba', 'PR');
insert into cidade4 values (2, 'Parnaiba', 'PI');
insert into cidade4 values (3, 'Videira', 'SC');
insert into cidade4 values (4, 'Imperatriz', 'MA');
insert into cidade4 values (5, 'Belo Horizonte', 'MG');
insert into cidade4 values (6, 'São Paulo', 'SP');
insert into cidade4 values (7, 'Paranapiacaba', 'SP');

update cidade4 
set nome = 'Mariana'
where id = 5;

update cidade4 
set nome = 'Londrina',
uf = 'PR'
where id = 4;

delete from cidade4 where id = 7;

update cidade4 set nome = 'Teste';

delete from cidade4;

select * from cidade4;
	