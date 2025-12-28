-- Last updated: 12/27/2025, 6:20:13 PM
# Write your MySQL query statement below
select w1.id from weather as w1
JOIN weather as w2 ON w1.recordDate = DATE_ADD(w2.recordDate, INTERVAL 1 DAY)
where w1.temperature > w2.temperature;