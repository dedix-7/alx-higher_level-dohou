-- A script that displays the number of records with id = 89 in the table
-- 'first_table' in a database of my MySQL server.
-- The database name will be passed as an argument of the mysql command.
SELECT COUNT(*) AS number_of_records FROM first_table WHERE id = 89;
