-- displays max temp  and a max value of each state
SELECT state, MAX(value) as 'max_temp' FROM temperatures GROUP BY state ORDER BY state;