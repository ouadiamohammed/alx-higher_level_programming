-- displays max temp of each state and a max value
SELECT state, MAX(value) as 'max_temp' FROM temperatures GROUP BY state ORDER BY state;