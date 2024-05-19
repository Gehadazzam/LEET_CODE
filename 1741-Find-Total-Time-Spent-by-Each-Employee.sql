# Write your MySQL query statement below
SELECT 
    event_day day, emp_id, sum(out_time-in_time) total_time
From
    Employees
Group by
    emp_id, event_day