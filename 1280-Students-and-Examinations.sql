# Write your MySQL query statement below
SELECT
    s.student_id,
    s.student_name,
    sub.subject_name,
    COUNT(e.student_id) attended_exams
FROM
    Students s
CROSS JOIN
    Subjects sub
LEFT OUTER JOIN 
    Examinations e
    ON 
        s.student_id = e.student_id AND sub.subject_name = e.subject_name
GROUP by
    s.student_id,
    s.student_name,
    sub.subject_name
ORDER by
    s.student_id,
    sub.subject_name;