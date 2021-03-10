# Write your MySQL query statement below
select
    e1.Name as Employee
from 
    employee e1
left join
    employee e2
on e1.ManagerId = e2.Id
where
    e1.Salary>e2.Salary
