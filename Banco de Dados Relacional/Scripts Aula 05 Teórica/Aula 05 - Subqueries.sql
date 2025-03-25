select * from cliente_subquery;
create table cliente_subquery (
	 id int auto_increment,
    nome varchar(100),
    genero char(01),
    nascimento date,
    salario decimal(10,2),
    email varchar(120) unique, 
    cidadeId int not null,
    constraint pkCliente primary key (id),
    constraint fkClienteCidade4 foreign key (cidadeId) references cidade5(id)
    on delete no action on update no action
);

create table vendas (
    numeroVenda int,
    data date,
    clienteId int,
    valorCompras decimal(10,2),
    primary key (numeroVenda) 
);

insert into vendas values (1, '2022-02-10', 4, 1000.00),
                          (2, '2022-02-10', 2, 500.00),
                          (3, '2022-03-11', 3, 100.00),
                          (4, '2022-03-11', 2, 400.00),
                          (5, '2022-03-11', 3, 200.00);



insert into cliente_subquery values (1, 'Helena Magalhães', 'F', '2000-01-01', 12500.99, 'helena@email.com', 2),
                           (2, 'Nicolas', 'M', '2002-12-10', 8500, 'nicolas@email.com', 3),
                           (3, 'Ana Rosa Silva', 'F', '1996-12-31', 8500, 'ana.rosa@email.com', 1),
                           (4, 'Tales Heitor Souza', 'M', '2000-10-01', 7689, 'tales.heitor@email.com', 1),
                           (5, 'Bia Meireles', 'F', '2002-03-14', 9450, 'bia.meireles@email.com', 2),
                           (6, 'Pedro Filho', 'M', '1998-05-22', 6800, 'pedro.filho@email.com', 5),
                           (7, 'Helena Magalhães', 'F', '1994-08-10', 8600, 'helena.magalhaes@email.com', 4);

-- Simples
select * from cliente_subquery
where cidadeId = (select id from cidade5 where nome = "Bagé");

select * from cliente_subquery
where cidadeId in (select id from cidade5
where nome = "Bagé" or nome = "Curitiba");

select nome, salario
from cliente_subquery
where salario < 7000
and exists
(select * from cliente_subquery where salario > 11000);

select * from cidade5;


-- any / all

select * from vendas;
select * from cidade5;
select * from cliente_subquery;

select * from cliente_subquery
where id > any (select distinct clienteid from vendas);


select * from cliente_subquery
where id > all (select distinct clienteid from vendas);

select cidadeid from cliente_subquery
intersect
select id from cidade5;

select cidadeid from cliente_subquery
inner join cidade5
on cidade5.id = cliente_subquery.cidadeid;

