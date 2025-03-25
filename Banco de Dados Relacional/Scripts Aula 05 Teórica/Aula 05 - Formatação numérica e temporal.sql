select * from funcionario2;

select salario, round(salario, 2), truncate(salario, 2)
from funcionario2;

select mod(10, 2), 4 div 2;

select curdate();

select day('2030-12-31'),
month('2030-12-31'),
year('2030-12-31');

select dayname('2030-12-31'), monthname('2030-12-31');
select curtime();

select hour('12:00:10');
select minute('12:00:10');
select adddate('2030-12-31', interval 30 day);
select adddate('2030-12-31', interval 1 month);
select datediff('2035-12-31', '2032-12-31');

