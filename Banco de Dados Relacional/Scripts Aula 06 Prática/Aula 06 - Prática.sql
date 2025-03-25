use aula;

-- Mostra que os dados ficam na ordem de inclusão
select * from pessoa;

-- Executa a consulta dos dados da "Vitoria"
select * from pessoa where nome = 'Vitoria';

-- Cria um índice para o nome da pessoa
create index idxPessoaNome on pessoa(nome);

-- Mostra os índices na tabela
show index from pessoa;

-- Plano de execução
explain select * from pessoa where nome = 'Vitoria';

-- Cria uma view
create view mostraFuncionario 
as 
    select nome as 'Nome', 
    genero as 'Gênero',  
    nascimento as 'Nascimento', 
    email as 'E-mail' 
    from funcionario;

select * from mostraFuncionario order by Nome;

-- Exemplo de função
delimiter $$
create function reajuste(salario decimal(10,2), percentual decimal(5,2))
returns decimal(10,2) deterministic
begin
    declare valorReajuste decimal(10,2) default 0;
    set valorReajuste = (salario * percentual) / 100;
    return (valorReajuste);
end $$
delimiter ;

-- Exemplo de uso de função
select salario, reajuste(salario, 10) from funcionario2;

-- Trigger disparada na inclusão
delimiter $$
create trigger funcionarioInclusao after insert 
on funcionario2
for each row
begin
    insert into auditoria values ('inclusão', new.matricula, null, new.salario, curdate());
end$$
delimiter ;

-- Mostra as triggers do Banco de Dados "aula"
show triggers from aula; 

-- Inclui um funcionário
insert into funcionario2 values (12, 'Ana Rosa Silva', 'F', '1996-12-31', 8500, 1, 1, 9, 'ana.rosa@email.com', 1);

-- Mostra os dados das tabelas "auditoria" e "funcionario"
select * from auditoria;
select * from funcionario2;

-- Exemplo de procedure
delimiter $$
create procedure incluiFuncionario(
    pmatricula int,
    pnome varchar(100),
    pgenero char(01),
    pnascimento date,
    psalario decimal(10,2),
    pdepartamento int,
    pcargo int,
    pgerente int,
    pemail varchar(120),
    pcidadeId int
)
begin
    declare mensagem varchar(100);
    set mensagem = 'OK';
    if exists (select * from funcionario2 where matricula = pmatricula) then
        set mensagem = 'Matrícula já existe';
    end if;
    if psalario < 0 then
		if mensagem = 'OK' then
			set mensagem = 'Salário Inválido';
		else
			set mensagem = CONCAT(mensagem, ', salário inválido');
		end if;
    end if;
    if length(trim(pnome)) = 0 then
		if mensagem = 'OK' then
			set mensagem = 'Nome está vazio';
		else
			set mensagem = CONCAT(mensagem, ', nome está vazio');
		end if;
    end if;
    if mensagem = 'OK' then
        insert into funcionario2 values (pmatricula, pnome, pgenero, pnascimento, psalario, pdepartamento, pcargo, pgerente, pemail, pcidadeId);
    end if;
end $$

call incluiFuncionario (9, 'Sofia Lima', null, '1999-12-23', 9578, 4, 4, 4, 'sofia.lima@email.com', 5);

show function status where db = 'aula';

-- Tabela para armazenar a simulação do reajuste de salário
create table simulacao (
    nome varchar(100), 
    salario decimal(10,2), 
    novoSalario decimal(10,2)
);

-- Cursor 
delimiter $$
create procedure simulaReajuste()
begin
    declare done boolean default false;  -- Variável para identificar o final do cursor
    declare vnome varchar(100); 
    declare vsalario decimal(10,2);
    declare vnovoSalario decimal(10,2);
    declare vdepartamento int;

    declare cursorFuncionario cursor 
        for select nome, departamento, salario
        from funcionario;

    declare continue handler 
        for not found set done = true; 
    
    open cursorFuncionario;
    
    leCursor: loop
        fetch cursorFuncionario 
            into vnome, vdepartamento, vsalario;
        if done then  -- Testa se o cursor chegou ao final
	    leave leCursor;  -- Sai do loop ao chegar no final
        end if;
        if vdepartamento = 1 then
	    set vnovoSalario = vsalario + reajuste(vsalario, 10);
        elseif vdepartamento = 2 then
	    set vnovoSalario = vsalario + reajuste(vsalario, 12);
        else
	    set vnovoSalario = vsalario + reajuste(vsalario, 8);
        end if;
        insert into simulacao values (vnome, vsalario, vnovoSalario);
    end loop;
close cursorFuncionario;
end $$
delimiter ;

-- Executa a procedure
call simulaReajuste();

select * from simulacao;
select * from funcionario;