-- A script that lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_shows.title - rating sum
-- Results must be sorted in descending order by the rating
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT tv_shows.title, COALESCE(temp.`rating sum`, 0) AS `rating sum`
FROM tv_shows
LEFT JOIN (
	    SELECT show_id, SUM(rating) AS `rating sum`
	    FROM ratings
	    GROUP BY show_id
) AS temp ON tv_shows.id = temp.show_id
ORDER BY `rating sum` DESC;
