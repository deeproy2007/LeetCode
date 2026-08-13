# Write your MySQL query statement below
with p as(select email ,count(email) as total from Person group by email)
select email from p where total>1;