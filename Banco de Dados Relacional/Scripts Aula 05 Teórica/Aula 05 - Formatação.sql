select * from cliente_subquery;

update cliente_subquery
set nome = " Helena Magalhães"
where id = 1;

update cliente_subquery
set nome = " Ana Rosa Silva"
where id = 3;

update cliente_subquery
set nome = " Tales Heitor Souza"
where id = 4;

delete from cliente_subquery where id = 7;

select length(nome), length(nascimento) from cliente_subquery;

select upper(nome), lower(nome) from cliente_subquery;

select ltrim(nome), rtrim(nome) from cliente_subquery;

select trim(both from nome), nome from cliente_subquery;

select substring(nome, 5), nome from cliente_subquery;

select substring(nome, 1, 3), nome from cliente_subquery;

select substring(nome, -5), nome from cliente_subquery;

select email, replace(email, '#', '@') from cliente_subquery;

select cast('2029-12-31' as date), cast('1000.99'as float);

