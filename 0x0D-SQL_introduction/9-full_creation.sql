-- A script that creates a table 'second_table' in
-- the database 'hbtn_0c_0' in my MySQL server and
-- adds multiple rows.
-- The database name will be passed as an argument to the mysql command
-- If second_table already exists, this script does not fail
-- I am not allowed to use the SELECT and SHOW statements
CREATE TABLE IF NOT EXISTS second_table (
       id INT,
       name VARCHAR(256),
       score INT
);
INSERT IGNORE INTO second_table (id, name, score)
VALUES
	(1, 'John', 10),
	(2, 'Alex', 3),
	(3, 'Bob', 14),
	(4, 'George', 8);
