use aula;

create table pessoa (
	nome varchar(50),
    email varchar(50)
);

insert into pessoa values ('Anabel', 'anabel@email.com');
insert into pessoa values ('Luis Afonso', 'luisafonso@email.com');
insert into pessoa values ('Alais', 'alais@email.com');
insert into pessoa values ('João Pedro', 'joaopedro@email.com');
insert into pessoa values ('Marcos', 'marcos@email.com');
insert into pessoa values ('Ulisses', 'ulisses@email.com');
insert into pessoa values ('Amadeu', 'amadeu@email.com');
insert into pessoa values ('Vitoria', 'vitoria@email.com');
insert into pessoa values ('Claudio', 'claudio@email.com');
insert into pessoa values ('Marcela', 'marcela@email.com');
insert into pessoa values ('Julia', 'julia@email.com');
insert into pessoa values ('Roberval', 'roberval@email.com');
insert into pessoa values ('Raiza', 'raiza@email.com');
insert into pessoa values ('Olavo', 'olavo@email.com');
insert into pessoa values ('Murilo', 'murilo@email.com');
insert into pessoa values ('Helena', 'melena@email.com');
insert into pessoa values ('Vitoria', 'vitoria@email.com');
insert into pessoa values ('Pedro', 'pedro@email.com');
insert into pessoa values ('Gabriela', 'gabriela@email.com');
insert into pessoa values ('Marilia', 'marilia@email.com');
insert into pessoa values ('Kevin', 'kevin@email.com');

select * from pessoa;

select * from pessoa where nome = 'Vitoria';

create index idxPessoa on pessoa(nome);

select * from pessoa where nome = 'Vitoria';

select * from funcionario2;

create view mostraFuncionario -- Serve para ocultar as tableas para certas pessoas
as
	select funcionario2.nome as nomeFunc,
    email, nascimento
    from funcionario2;
    
select salario from mostraFuncionario;

set autocommit = off;
start transaction;
insert into pessoa values ('zanana', 'teste@teste.com');
select * from pessoa;
rollback;



