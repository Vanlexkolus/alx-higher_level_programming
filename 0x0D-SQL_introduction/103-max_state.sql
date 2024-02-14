-- a script that displays the max temperature of each state (ordered by State name).
SELECT city, AVG((value * 9/5) + 32) AS avg_temp
FROM temperatures
WHERE (month = 7 OR month = 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
