-- query that displays avg temp by city ordered by temp desc
SELECT city, AVG(value) as 'avg_temp' FROM temperatures GROUP BY city ORDER BY `avg_temp` DESC