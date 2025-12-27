-- Last updated: 12/26/2025, 6:37:25 PM
# Write your MySQL query statement below
SELECT u.unique_id, e.name FROM Employees AS e
LEFT JOIN EmployeeUNI as u ON e.id = u.id;