SELECT department, employee_number, salary, rank() OVER (PARTITION BY department ORDER BY salary DESC) FROM employee_salary

select department, avg(salary) from employee_salary GROUP BY department


SELECT department, employee_number, salary 
FROM employee_salary 
ORDER BY department DESC, salary DESC;



SELECT salary, sum(salary) OVER () FROM employee_salary;

SELECT salary, sum(salary) OVER (ORDER BY salary) FROM employee_salary;


SELECT row_to_json(employee_salary) FROM employee_salary;

SELECT row_to_json(row(employee_number, salary))
FROM employee_salary
LIMIT 3;



SELECT row_to_json(t)
FROM ( 
SELECT employee_number, salary from employee_salary ) 
t
LIMIT 3;


SELECT array_to_json(array_agg(row_to_json(t)))
    FROM (
      SELECT employee_number, salary FROM employee_salary
    ) t











SELECT department, employee_number, salary, rank() 
OVER (PARTITION BY department ORDER BY salary DESC) 
FROM employee_salary;


SELECT department,  cast(salary as float)/cast(total_salary as float), salary, total_salary  from (
SELECT department, salary, sum(salary) 
OVER (PARTITION BY department)  as total_salary 
FROM employee_salary
) a;


SELECT * FROM employee_salary where   salary  in (
SELECT  max(salary) from employee_salary 
 
);




SELECT * FROM employee_salary where (department, salary) in (
SELECT department, max(salary) from employee_salary 
group by department
);

SELECT department, salary FROM (
SELECT department, salary FROM employee_salary
) WHERE (department, salary) 
 
SELECT department, count(*) as C, sum(salary) as S , avg(salary) FROM employee_salary group by department


