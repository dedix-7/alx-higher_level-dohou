-- A script that imports a table dump into a database 'hbtn_0c_0'
-- and then displays the top three of cities temperature during
-- July and Augustt ordered by temperature (descending).
-- First command used:
-- mysql -u root -p hbtn_0c_0 < temperatures.sql;
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month=7 OR month=8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
