SELECT ed.first_name, ed.last_name, es.occupation, es.salary
FROM employee_demographics ed
INNER JOIN employee_salary es ON ed.employee_id = es.employee_id;

SELECT ed.first_name, ed.last_name, ed.gender, ed.age
FROM employee_demographics ed
LEFT JOIN employee_salary es ON ed.employee_id = es.employee_id
WHERE es.employee_id is null;

SELECT ed.first_name, ed.last_name, ed.age, es.occupation, es.salary
FROM employee_demographics ed
LEFT JOIN employee_salary es ON ed.employee_id = es.employee_id;

SELECT es.first_name, es.last_name, es.occupation, es.salary
FROM employee_salary es
RIGHT JOIN employee_demographics ed ON ed.employee_id = es.employee_id;

SELECT ed.gender, AVG(es.salary) AS average_salary
FROM employee_demographics ed
INNER JOIN employee_salary es ON ed.employee_id = es.employee_id
GROUP BY ed.gender;

SELECT ed.first_name, ed.last_name, ed.age, es.occupation, es.salary
FROM employee_demographics ed
INNER JOIN employee_salary es ON ed.employee_id = es.employee_id
WHERE ed.age < 40;

SELECT ed.first_name, ed.last_name, es.occupation, es.salary
FROM employee_demographics ed
INNER JOIN employee_salary es ON ed.employee_id = es.employee_id
WHERE es.salary > 60000;

SELECT SUM(es.salary) AS total_salary
FROM employee_salary es
WHERE es.dept_id = 1;

SELECT ed.first_name, ed.last_name, ed.age, es.occupation, es.salary
FROM employee_demographics ed
INNER JOIN employee_salary es ON ed.employee_id = es.employee_id
WHERE es.dept_id = 1;

SELECT ed.first_name, ed.last_name, ed.age, es.salary
FROM employee_demographics ed
INNER JOIN employee_salary es ON ed.employee_id = es.employee_id
WHERE ed.age > 45 AND es.salary < 50000;









