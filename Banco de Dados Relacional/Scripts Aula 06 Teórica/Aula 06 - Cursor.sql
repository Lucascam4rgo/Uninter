-- Tabela para armazenar a simulação do reajuste de salário
create table simulacao (
    nome varchar(100), 
    salario decimal(10,2), 
    novoSalario decimal(10,2)
);



delimiter $$
create procedure simulaReajuste()
begin
	declare done boolean default false; -- Variável para identificar o final do cursor
    declare vnome varchar(100);
    declare vsalario decimal(10,2);
    declare vnovoSalario decimal(10, 2);
    declare vdepartamento int;
    
    declare cursorFuncionario cursor
    for select nome, departamento, salario
		from funcionario2;
	
    declare continue handler
    for not found set done = true;
    
    open cursorFuncionario;
    
    leCursor: loop
		fetch cursorFuncionario
        into vnome, vdepartamento, vsalario;
			if done then -- testa se o cursor chegou ao final.
				leave leCursor; -- sai do loop ao chegar no final
			end if;
            
            if vdepartamento = 1 then
				set vnovosalario = vsalario * 1.10;
			elseif vdepartamento = 2 then
				set vnovosalario = vsalario * 1.12;
			else
				set vnovosalario = vsalario * 1.08;
			end if;
			
            insert into simulacao
				values (vnome, vsalario, vnovosalario);
		end loop;
	close cursorFuncionario;
end$$
    
delimiter ;

call simulaReajuste;

select * from simulacao;