-- comando para mostrar os bds
show databases;

/*

Comentários de várias linhas

*/

/* create database aula;
use aula;

select database();
*/

create table exemplo (
	id int,
    nome varchar(100)
);

show tables;

insert into exemplo (id, nome) values (1, "Lucas");

select * from exemplo;


