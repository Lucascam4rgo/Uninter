select * from cidade5;
select * from pergunta;
select * from estado;
select * from funcionario2;

create table pergunta (
    id int,
    pergunta varchar(100),
    primary key(id)
);

create table estado (
	id int,
    nome varchar(50),
    sigla char(02),
    primary key(id)
);

create table cidade5 (
	id int,
    nome varchar(100),
    estadoId int,
    primary key(id)
);

create table funcionario2 (
    matricula int not null,
    nome varchar(100),
    genero char(01),
    nascimento date,
    salario decimal(10,2),
    departamento int,
    cargo int,
    gerente int,
    email varchar(120),
    cidadeId int,
    constraint pkFuncionario primary key (matricula)
);

insert into funcionario2 values (1, 'Ana Rosa', 'F', '1996-12-31', 8500, 1, 1, null,'ana.rosa@email.com', 1),
                               (2, 'Tales Heitor', 'M', '2000-10-01', 7689, 1, 2, 1, 'tales.heitor@email.com', null),
                               (3, 'Bia Meireles', 'F', '2002-03-14', 9450, 1, 2, 1, 'bia.meireles@email.com', 2),
                               (4, 'Pedro Filho', 'M', '1998-05-22', 6800, 3, 3, 2, 'pedro.filho@email.com', 4),
                               (5, 'Helena Magalhães', 'F', '2000-01-01', 12500.99, 4, 5, 2, 'helena@email.com', 6),
                               (6, 'Nicolas Pinto', 'M', '2002-12-10', 8500, 6, 3, null, 'nicolas.pinto@email.com', 5);

insert into estado values (1, 'Paraná', 'PR');
insert into estado values (2, 'São Paulo', 'SP');
insert into estado values (3, 'Pernambuco', 'PE');
insert into estado values (4, 'Pará', 'PA');
insert into estado values (5, 'Rio Grande do Sul', 'RS');

insert into cidade5 values (1, 'Bagé', 5);
insert into cidade5 values (2, 'Curitiba', 1);
insert into cidade5 values (3, 'Recife', 3);
insert into cidade5 values (4, 'São Paulo', null);
insert into cidade5 values (5, 'Porto Alegre', null);
insert into cidade5 values (6, 'Olinda', 3);

insert into pergunta values (1, 'Qual a sua função?');
insert into pergunta values (2, 'Avalie a sua gerência.');

select cidade5.nome as nomeCidade, estado.nome as nomeEstado
from cidade5
inner join estado
on cidade5.estadoId = estado.id;

select cidade5.nome as nomeCidade, estado.nome as nomeEstado
from cidade5
left join estado
on cidade5.estadoId = estado.id;

select cidade5.nome as nomeCidade, estado.nome as nomeEstado
from cidade5
right join estado
on cidade5.estadoId = estado.id;

-- cross join
select cidade5.nome as nomeCidade, estado.nome as estadoNome
from cidade5, estado
order by nomeCidade;

-- self join

select funcionario2.nome as nomeFunc, gerente.nome as gerenteNomeFunc
from funcionario2
inner join funcionario2 gerente
on funcionario2.gerente = gerente.matricula;

select funcionario2.nome as nomeFunc, gerente.nome as gerenteNomeFunc
from funcionario2
left join funcionario2 gerente
on funcionario2.gerente = gerente.matricula;

