-- A script that lists all records of a table 'second_table'
-- of a database 'hbtn_0c_0' in my MySQL server.
-- Records should be ordered by score (top first).
-- Results are dislayed in descending order.
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
