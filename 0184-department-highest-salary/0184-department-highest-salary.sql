# Write your MySQL query statement below
with p as ( select e.name as Employee,e.salary as Salary,d.name as Department, dense_rank() over (partition by d.name order by e.salary desc ) as RankS from Employee e left join Department d on e.departmentId = d.id )
select Department,  Employee, Salary from p where RankS <= 1;