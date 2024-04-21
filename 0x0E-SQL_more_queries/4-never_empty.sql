-- A script that creates the table id_not_null on your MySQL server.
-- It assigns a default value to a variable.
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 0,
	name VARCHAR(256)
);
