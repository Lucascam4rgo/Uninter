select * from cidade3;
select * from cliente2;

/*insert into cidade3 values (4, 'Imperatriz', 'MA');
insert into cidade3 values (5, 'Belo Horizonte', 'MG');
insert into cidade3 values (6, 'São Paulo', 'SP');
insert into cidade3 values (7, 'Paranapiacaba', 'SP');
*/

select * from cliente2
where cidadeId = 3
and salario > 2000;

select nome, salario from cliente2
where cidadeId = 1
or cidadeId = 3
or cidadeId = 5;

select nome, salario from cliente2
where cidadeId in (1, 3, 5);

select nome, salario
from cliente2
where salario >= 2000
and salario <= 5000;

select nome, salario
from cliente2
where salario between 2500 and 5000;

select nome, salario
from cliente2 where
salario between 2500 and 6000
order by nome;

select nome, salario
from cliente2 where
salario between 3000 and 6000
order by salario;

select nome, salario
from cliente2 where
salario between 2000 and 6000
order by 2;






