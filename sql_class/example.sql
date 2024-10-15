create table employee_demographics(
employee_id INT NOT NULL,
first_name varchar(50),
last_name varchar(50),
age int,
genter varchar(10),
birth_date date,
primary key(employee_id)
);
SELECT *
FROM employee_demographics
WHERE MONTHNAME(birth_date) = 'March';
