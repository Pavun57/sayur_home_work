SELECT AVG(salary) AS average_salary
FROM employee_salary WHERE dept_id = 1;

SELECT first_name, last_name, salary
FROM employee_salary WHERE dept_id = 1 ORDER BY salary DESC;

SELECT first_name, last_name, salary
FROM employee_salary
WHERE salary > 50000;

SELECT COUNT(*) AS employee_count
FROM employee_salary
WHERE dept_id = 1;

SELECT first_name, last_name, occupation
FROM employee_salary
WHERE dept_id IS NULL;

SELECT first_name, last_name, occupation
FROM employee_salary
WHERE occupation LIKE '%Manager%' OR occupation LIKE '%Director%';

SELECT SUM(salary) AS total_expenditure
FROM employee_salary;

SELECT first_name, last_name, salary
FROM employee_salary
ORDER BY salary DESC;

SELECT MIN(salary) AS min_salary, MAX(salary) AS max_salary
FROM employee_salary
WHERE dept_id = 1;

SELECT COUNT(*) AS low_salary_count
FROM employee_salary
WHERE salary < 30000;