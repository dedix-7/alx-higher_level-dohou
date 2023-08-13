-- A script that creates a database and a table
-- Create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use the database.
USE hbtn_0d_usa;
-- Create table
CREATE TABLE IF NOT EXISTS cities (
	id INT NOT NULL AUTO_INNCREMENT PRIMARY KEY UNIQUE,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY(states) REFERENCES states(state_id)
);
