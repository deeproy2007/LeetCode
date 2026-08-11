# Write your MySQL query statement below
with c as (select e.name as employee,m.name as manager,e.salary as empsalary,m.salary as msalary from Employee as e left join Employee as m 
on e.managerId=m.id)
select employee from c where empsalary>msalary;