select * from funcionario2;

select count(*), count(genero) from funcionario2;

select sum(salario) from funcionario2
where departamento = 1;

select min(salario), max(salario) from funcionario2;
select min(salario), nome from funcionario2;

select avg(salario) from funcionario;

select departamento, sum(salario) from funcionario2
group by departamento;

select departamento, cargo, sum(salario) from funcionario2
group by departamento, cargo;

select departamento, sum(salario) from funcionario2
group by departamento
having sum(salario) > 20000;

select departamento, sum(salario) from funcionario2
group by departamento
having sum(salario) > 20000
order by 2 asc;

select nome, salario from funcionario2
where salario = (select min(salario) from funcionario2);

select min(nascimento) from funcionario2;

insert into funcionario2 values (7, 'Leonardo Timbo', null, '2001-07-02', 7850.1280, 2, 3, null, 'leonardo.timbo@email.com', 2),
                               (8, 'Lucas Goes', 'M', '2002-03-02', 8834.9880, 3, 4, 4, 'lucas.goes@email.com', 5),
                               (9, 'Sofia Lima', null, '1999-12-23', 9578.549, 4, 4, 1,'sofia.lima@email.com', 5),
                               (10, 'Nicolas Figueira', 'M', '1997-06-01', 12340.1209, 3, 2, 1,'nicolas.figueira@email.com', 3),
                               (11, 'Helena Arcanjo', 'F', '1998-11-20', 6320.9876, 2, 2, 5, 'helena.arcanjo@email.com', 7);


select * from funcionario2;