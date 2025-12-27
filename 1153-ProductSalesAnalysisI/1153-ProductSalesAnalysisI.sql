-- Last updated: 12/26/2025, 6:37:26 PM
# Write your MySQL query statement below
SELECT p.product_name,s.year,s.price FROM Sales AS s
LEFT JOIN Product AS p ON s.product_id = p.product_id;