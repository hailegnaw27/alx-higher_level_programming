-- 101-avg_temperatures.sql

-- This script displays the average temperature by city ordered by temperature (descending)

SELECT city, AVG(temperature) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
