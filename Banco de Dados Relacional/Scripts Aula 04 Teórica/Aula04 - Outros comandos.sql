select f.nome as NomeFunc from funcionario2 as f
where f.cidadeId = 1;

select * from funcionario2 limit 3;

select funcionario2.nome as NomeFunc from funcionario2
union all -- union/union all
select cidade5.nome from cidade5;

select funcionario2.nome as nomeFunc,
case
	when funcionario2.genero = "F" then 'Feminino'
    when funcionario2.genero = "M" then 'Masculino'
end as 'Genero'
from funcionario2;


