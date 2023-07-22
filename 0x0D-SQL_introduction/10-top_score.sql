-- A script that lists al records of a table 'second_table'
-- of a database 'hbtn_0c_0' in my MySQL server
-- Records should be ordered by score (top first)
-- Results are dislayed in descending order
-- SELECT * FROM second_table ORDER BY score DESC, name DESC;
SELECT score, name FROM second_table ORDER BY score DESC;
