-- Last updated: 12/27/2025, 5:13:48 PM
# Write your MySQL query statement below
SELECT v.customer_id, COUNT(v.visit_id) as count_no_trans FROM Visits AS v
LEFT JOIN Transactions AS t ON v.visit_id = t.visit_id
Where t.transaction_id is null
Group by v.customer_id;