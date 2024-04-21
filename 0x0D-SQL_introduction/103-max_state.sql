-- A script that imports a table dump into a database 'hbtn_0c_0'
-- and then display the max temperature of each state (ordered by State name).
-- First command used:
-- mysql -u root -p hbtn_0c_0 < temperatures.sql;
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
