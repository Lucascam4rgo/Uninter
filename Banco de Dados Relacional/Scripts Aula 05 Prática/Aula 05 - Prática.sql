-- Mod e div
select mod(4,2) as 'Resto divisão',
    mod(5,2) as 'Resto divisão', 
    4 div 2 as 'Quociente',
    5 div 2 as 'Quociente';

use aula;

-- Round, truncate, mod e div
select salario,
    round(salario),
    round(salario,2),
    round(salario, 1),
    truncate(salario, 0),
    truncate(salario, 1),
    truncate(salario, 2)
    from funcionario2;

-- Formatação de texto
select nome,
    upper(nome),
    lower(nome), 
    length(nome),
    ltrim(nome),
    rtrim(nome), 
    substring(nome, 5),
    substring(nome, 1, 3),
    nascimento,
    length(nascimento), 
    email,
    replace(email, '#', '@')
    from cliente_subquery;

-- Funções de agregação
-- Count(*) e count null
select count(*),
    count(genero)
    from funcionario2;
    
select * from funcionario2;

-- Conversão de valoes
select cast('20000101' as date), 
    cast('1000.00' as decimal),
    cast('20:15' as time);

select curdate(),
    curtime(),
    now(), 
    date(curdate()),
    date(now());

-- Funções referentes ao dia
select curdate(), curtime(), now(), date(curdate()), date(now());
select curdate(), day(curdate()), dayname(curdate()), dayofweek(curdate()), dayofyear(curdate()), last_day(curdate());
select month(curdate()), monthname(curdate()), year(curdate());
select curdate(), now(), week(curdate()), weekday(now()), weekday(curdate());
select curdate(), adddate(curdate(), interval 31 day), adddate(curdate(), interval 1 month);
select curdate(), datediff('2022-01-01', curdate()), datediff(curdate(), '2022-01-01');
select curdate(), date_format(curdate(), '%w %m %y'), date_format('2022-01-01 20:15:00', '%h:%i:%s');

-- Funções de hora
select curtime(), time(curtime()), hour(curtime()), minute(curtime()), second(curtime()), microsecond(curtime());
select addtime('01:00:00.999999', '02:00:00.999998');
select timestamp('2003-12-31'), timestamp('2003-12-31 12:00:00', '12:00:00');
select curdate(), curtime(), timestampadd(minute, 30, curdate());
select timediff('2021-12-31 23:59:59.000001', '2021-12-31 01:01:01.000002');
select time_format('20:30:00', '%h %i');

-- Contando com filtro
select count(*) from funcionario2
    where genero = 'M';

-- Sum salário
select sum(salario) from funcionario2;

-- Min
select min(salario), min(nascimento) from funcionario2;

-- Max
select max(salario), max(nascimento) from funcionario2;

-- Média
select avg(salario) from funcionario2;

-- Group by: Contando funcionários do departamento
select departamento, count(*) from funcionario2 
group by departamento
order by departamento;

-- having
select departamento, count(*) from funcionario2 
    group by departamento 
    having count(departamento) > 2;

-- Group by por gênero
select genero, avg(salario) from funcionario2 
    group by genero;

-- Subconsultas
select nome, salario from funcionario2
    where salario = (select max(salario) from funcionario2);

select nome, cidadeId from cliente_subquery
    where cidadeId = (select id from cidade5 where nome = 'Bagé');

-- Usando o in
select nome, cidadeId  from cliente_subquery 
    where cidadeId in (select id from cidade5 where nome = 'Curitiba' or nome = 'Imperatriz');

-- Não Curitiba e não Imperatriz
select nome, cidadeId  from cliente_subquery
    where cidadeId not in (select id from cidade5 where nome = 'Curitiba' or nome = 'Imperatriz');

-- Exists
-- < 7000 > 11000
select nome, genero, salario from cliente_subquery 
    where salario < 7000
    and exists (select * from cliente where salario > 11000);

-- Any
-- id cliente > id cliente venda
select id, nome, genero from cliente_subquery
    where id > any (select distinct clienteId from vendas);

-- All
select id, nome, genero from cliente_subquery
    where id > all (select distinct clienteId from vendas);

-- Subconsulta correlacionada
-- salario > any salario do mesmo gênero
select id, nome, genero, salario from cliente_subquery c
    where salario > any (select salario from cliente_subquery where genero = c.genero);

select * from cliente_subquery;

-- Controle de acesso
-- Criando o usuário "aluno"
create user 'aluno'@'localhost' identified by '123';

-- Atualizando os privilégios
flush privileges;

-- Mostrando os usuários existentes
select user, host from mysql.user;

-- Mostrando os privilégios do usuário "aluno"
show grants for 'aluno@localhost';

revoke all, grant option from 'aluno@localhost';
flush privileges;
show grants for 'aluno@localhost';

-- Atribuindo algumas permissões
grant select, insert, delete on aula.* to 'aluno@localhost';
flush privileges;
show grants for 'aluno@localhost';
show grants for 'aluno';

-- Alterando os privilégios do usuário "aluno"
grant all privileges on *.* to 'aluno@localhost';
flush privileges;

-- Retirando a permissão de update
revoke update on aula.* from 'aluno@localhost';
flush privileges;
show grants for 'aluno@localhost';

-- Excluindo o usuário "aluno"
drop user 'aluno@localhost';