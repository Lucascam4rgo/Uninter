delimiter $$
create function parImpar(numero int)
returns char(05) deterministic
begin
	declare tipo char(05) default null;
    set tipo = 'Impar';
    if numero mod 2 = 0 then
		set tipo = 'Par';
	end if;
    return (tipo);
end$$

delimiter ;

select parImpar(10), parImpar(3);