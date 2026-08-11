# Write your MySQL query statement below
with p as (select d.name as Department,e.name as Employee,e.Salary as Salary, dense_rank() over (partition by d.name order by e.Salary desc) as
'Salarys' from Employee e join Department d
on e.departmentId=d.id)
select Department,Employee,Salary from p where Salarys <= 3;
