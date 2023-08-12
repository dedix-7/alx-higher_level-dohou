-- A script that creates a database 'hbtn_0d_usa' and the table 'states' (in the database 'hbtn_0d_usa') on my MySQL server.
-- Create the database.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use the database.
USE hbtn_0d_usa;
-- Create a table 'states' in the database.
CREATE TABLE IF NOT EXISTS states (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
