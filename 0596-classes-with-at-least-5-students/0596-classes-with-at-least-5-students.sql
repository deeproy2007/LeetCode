# Write your MySQL query statement bel
with p as (select class,count(student) as total from Courses group by class)
select class from p where total >= 5;