select * from funcionario2;
select * from auditoria;

create table auditoria (
    acao char(10),  -- Será inclusão, exclusão ou alteração
    matricula int,
    salarioAntigo decimal(10,2),
    salarioNovo decimal(10,2),
    dataOperacao date
);

delimiter $$
create trigger alterafuncionario after update
on funcionario2
for each row
begin 
	insert into auditoria values
    ('alteracao', new.matricula, old.salario, new.salario, curdate());
end$$
delimiter ;

select salario from funcionario2 where matricula = 1;

update funcionario2
set salario = 9500
where matricula = 1;

select * from auditoria;