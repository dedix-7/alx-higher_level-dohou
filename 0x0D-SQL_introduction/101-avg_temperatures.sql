-- A script that imports a table dump into a database 'hbtn_0c_0'
-- and then display the average temperature (Farenheit) by city
-- ordered by temperature (descending)
-- USE hbtn_0c_0;
-- SOURCE ./temperatures.sql;
-- First command used:
-- mysql -u root -p hbtn_0c_0 < temperatures.sql;
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
