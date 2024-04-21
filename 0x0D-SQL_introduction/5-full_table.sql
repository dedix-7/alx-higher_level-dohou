-- A script that prints the full description of the table
-- 'first_table' from the database 'hbtn_0c_0' in my MySQL server.
-- The database name will be passed as an argument of the mysql command.
-- I am not allowed to use the DESCRIBE or EXPLAIN statements.
-- SHOW COLUMNS FROM first_table;
-- DESCRIBE first_table;
-- DESC first_table;
SHOW CREATE TABLE first_table;
-- SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'hbtn_0c_0' AND TABLE_NAME = 'first_name';
