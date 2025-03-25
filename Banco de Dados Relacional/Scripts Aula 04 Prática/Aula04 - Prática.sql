use aula;

create table cliente3 (
    id int auto_increment,
    nome varchar(100),
    genero char(01),
    nascimento date,
    salario decimal(10,2),
    email varchar(120) unique, 
    cidadeId int not null,
    constraint pkCliente primary key (id),
    constraint fkClienteCidade3 foreign key (cidadeId) references cidade5(id)
    on delete no action on update no action
);

insert into cliente3 values (1, 'Helena Magalhães', 'F', '2000-01-01', 12500.99, 'helena@email.com', 2),
                           (2, 'Nicolas', 'M', '2002-12-10', 8500, 'nicolas@email.com', 3),
                           (3, 'Ana Rosa Silva', 'F', '1996-12-31', 8500, 'ana.rosa@email.com', 1),
                           (4, 'Tales Heitor Souza', 'M', '2000-10-01', 7689, 'tales.heitor@email.com', 1),
                           (5, 'Bia Meireles', 'F', '2002-03-14', 9450, 'bia.meireles@email.com', 2),
                           (6, 'Pedro Filho', 'M', '1998-05-22', 6800, 'pedro.filho@email.com', 5),
                           (7, 'Helena Magalhães', 'F', '1994-08-10', 8600, 'helena.magalhaes@email.com', 4);
                           

update funcionario2
    set cidadeId = (select id from cidade5 where nome = 'Recife')
    where matricula = 2;
    

update funcionario2
    set nome = 'João da Silva',
    departamento = 3
    where matricula = 2;

insert into cidade5 (id, nome, estadoId) values (7, 'Londrina', 1);

delete from cliente3 where id = 5;

delete from cliente3 where nome = 'Helena Magalhães';

delete from funcionario2 where departamento = 1 and genero = 'M';

select * from funcionario2;
select * from cliente3;
select * from cidade5;

delete from cidade5 where id = 6;
    
delete from cliente3 where cidadeId in 
    (select id from cidade5 where nome = 'Curitiba');

delete from cliente3;

truncate table cliente3;

-- Filtro
select * from cliente3 where genero = 'F';

-- And / or
select * from funcionario2 where salario >= 5000 and salario <= 8000;

-- Null / not null
select * from cidade5 where estadoId is not null;

-- Like
select * from cliente3 where nome like '%Silva%';

-- In
select * from cliente3 where cidadeId in (1, 2, 4);
select * from funcionario2 where cidadeId = 1 or cidadeId = 2 or cidadeId = 4;

-- Between
select * from funcionario2 where cidadeId between 1 and 4;
-- ou 
select * from funcionario2 where cidadeId >= 1 and cidadeId <= 4;
select * from funcionario2 order by nome asc, salario asc; -- Salário é um critério secundário 
select * from funcionario2 order by 3 asc;

-- Limit
select * from funcionario2 LIMIT 3;
select * from funcionario2 LIMIT 3, 2; -- Pula 3 e coloca 2
-- Comando case
select nome,
    case
        when genero = 'M' then 'Masculino'
        when genero = 'F' then 'Feminino'
        else 'Outros'
    end as 'Gênero'
from funcionario2;

select nome, nascimento from cliente3
union 
select nome, nascimento from funcionario2;

select nome, nascimento, 'cliente' from cliente3
union all
select nome, nascimento, 'funcionario' from funcionario2
order by 1;

-- Distinct
select nome from cliente3 order by nome;
select distinct nome from cliente3 order by nome;

-- Distinct com mais colunas
select nome, email from cliente3 order by nome;
select distinct nome, email from cliente3 order by nome; -- Remove duplicatas

-- Inner join - equi-non
select estado.nome, cidade5.nome, sigla from cidade5 
    inner join estado
    on cidade5.estadoId = estado.id;

select * from cidade5;

-- Usando where
select cidade5.nome, estado.nome, sigla from cidade5, estado
    where cidade5.estadoId = estado.id;

-- Left join inclusive
select cidade5.nome, estado.nome, sigla from cidade5 
    left join estado
    on cidade5.estadoId = estado.id;

-- Left join exclusive
select cidade5.nome, estado.nome, sigla from cidade5 
    left join estado
    on cidade5.estadoId = estado.id
    where estado.id is null;

-- Right join inclusive
select cidade5.nome, estado.nome, sigla from cidade5 
    right join estado
    on cidade5.estadoId = estado.id;

-- Right join exclusive
select cidade5.nome, estado.nome, sigla from cidade5 
    right join estado
    on cidade5.estadoId = estado.id
    where cidade5.estadoId is null;

-- Full join (o MySQL não suporta o full join)
select cidade5.nome, estado.nome, sigla from cidade5 
    full join estado
    on cidade5.estadoId = estado.id;

-- Gerando o full join
select cidade5.nome, estado.nome, sigla from cidade5 
    left join estado
    on cidade5.estadoId = estado.id
    union
    select cidade5.nome, estado.nome, sigla from cidade5 
        right join estado
        on cidade5.estadoId = estado.id
    where cidade5.estadoId is null;

-- Cross join
select nome, pergunta from pergunta
    cross join funcionario2;

select * from funcionario2;

-- Self join com inner join
select funcionario2.nome, gerente.nome as 'gerente' from funcionario2 
    inner join funcionario2 as gerente
    on funcionario2.gerente = gerente.matricula
    order by funcionario2.nome;

-- Self join com left join
select funcionario2.nome, gerente.nome from funcionario 
    left join funcionario2 as gerente
    on funcionario2.gerente = gerente.matricula
    order by funcionario2.nome;

-- Join com várias tabelas
select cidade5.nome, estado.nome, funcionario2.nome from funcionario2
    inner join cidade5 
    on funcionario2.cidadeId = cidade.id
    inner join estado
    on cidade.estadoId = estado.id
    order by nome;

select cidade5.nome, estado.nome, sigla from cidade 
    full join estado
    on cidade.estadoId = estado.id
    where cidade.estadoId is null
    or estado.id is null;

select funcionario2.nome, salario, salario * 1.10 from funcionario2;

select funcionario2.nome as 'Nome do funcionário', 
    salario as 'Salário atual',
    salario * 1.10 as 'Novo salário'
    from funcionario;

select funcionario2.nome as 'Nome do funcionário', nome as 'Nome da cidade' from funcionario f
    inner join cidade5 c
    on f.cidadeId = c.id;
