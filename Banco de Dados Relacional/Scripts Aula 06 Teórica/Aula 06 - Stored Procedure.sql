use aula;

create table if not exists cartela(
concurso int, numero int);

delimiter $$
create procedure geraNemeros(nroInicial int, nroFinal int, nroConcurso int)
	begin
		declare nroGerado int default 0;
        declare i int default 0;
        while i < 6 do
			set nroGerado = (select floor(rand() * nroFinal) + nroInicial);
			if not exists (select * from cartela where numero = nroGerado) then
				insert into cartela values (nroConcurso, nroGerado);
                set i = i + 1;
			end if;
	end while;
end$$

delimiter ;

call geraNemeros(1, 60, 100);

select * from cartela;