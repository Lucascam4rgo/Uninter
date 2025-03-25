select * from funcionario2;

create user 'aluno@localhost' identified by '123';

flush privileges;

show grants for 'aluno@localhost';

grant select, insert on aula.* to 'aluno@localhost';