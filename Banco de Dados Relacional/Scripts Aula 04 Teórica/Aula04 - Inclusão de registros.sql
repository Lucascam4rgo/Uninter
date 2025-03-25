use aula;

show tables;

create table cidade3 
(id int,
nome varchar(100) not null,
uf char(02), 
constraint pkCidade primary key (id)
);

create table cliente2 (
	id int auto_increment,
    nome varchar(100),
    cidadeId int not null,
    constraint pkCliente primary key (id),
    constraint fkClienteCidade2 foreign key (cidadeId)
    references cidade3(id)
);

-- insert sintaxe completa
insert into cidade3 (id, nome, uf) values (1, "Bagé", "RS");
-- Reduzido
insert into cidade3 values (2, "Parnaiba", "PI");
-- Insert de algumas colunas
insert into cidade3 (id, nome) values (3, "Imperatriz");
select * from cidade3;

insert into cliente2 (nome, cidadeId) values ("Pedro", 1);

insert into cliente2 (nome,cidadeId) values ("Nicolas", 2),
("Maria Eduarda", 1), ("Beatriz", 3);

insert into cliente2 (id, nome, cidadeId) values (2, "Maria", 3);

insert into cliente2 (nome,cidadeId) values ("Lucas", 2),
("Bruna", 3), ("Lívia", 3);

alter table cliente2
add genero char(01),
add nascimento date,
add salario decimal(10,2) unsigned default 0,
add email varchar(120) unique;

update cliente2
set genero = "M",
nascimento = "1990-05-15",
salario = 3000.00,
email = "pedro@email.com"
where id = 1;

update cliente2
set genero = "F",
nascimento = "1995-08-23",
salario = 3500.00,
email = "maria@email.com"
where id = 2;

UPDATE cliente2 SET genero = 'M', nascimento = '1988-03-10', salario = 4500.75, email = 'nicolas@email.com' WHERE nome = 'Nicolas';

UPDATE cliente2 SET genero = 'F', nascimento = '2000-12-05', salario = 3200.00, email = 'mariaeduarda@email.com' WHERE nome = 'Maria Eduarda';

UPDATE cliente2 SET genero = 'F', nascimento = '1992-09-17', salario = 3500.20, email = 'beatriz@email.com' WHERE nome = 'Beatriz';

UPDATE cliente2 SET genero = 'M', nascimento = '1996-01-25', salario = 4000.00, email = 'lucas@email.com' WHERE nome = 'Lucas';

UPDATE cliente2 SET genero = 'F', nascimento = '1994-11-03', salario = 2900.50, email = 'bruna@email.com' WHERE nome = 'Bruna';

UPDATE cliente2 SET genero = 'F', nascimento = '1999-08-14', salario = 3300.80, email = 'livia@email.com' WHERE nome = 'Lívia';

update cliente2 set cidadeId = 4 where nome = 'Nicolas' or nome = 'Beatriz';

update cliente2 set cidadeId = 5 where nome = 'Lucas';

update cliente2 set cidadeId = 6 where nome = 'Pedro';

update cliente2 set cidadeId = 7 where nome = 'Maria';

select * from cliente2;

create table funcionario (
	id int,
    nome varchar(100),
    cidadeId int not null,
    constraint fkFuncCidade foreign key (cidadeId)
    references cidade3(id)
);



insert into funcionario (id, nome, cidadeId, ) select id, nome, cidadeId
from cliente2;

select * from funcionario;

