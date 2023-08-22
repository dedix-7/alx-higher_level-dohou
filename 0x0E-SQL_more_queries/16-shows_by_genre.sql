-- A script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
-- If a show doesn’t have a genre, display NULL in the genre column
-- Each record should display: tv_shows.title - tv_genres.name
-- Results must be sorted in ascending order by the show title and genre name
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command

-- If there's no genre associated with a show, COALESCE ensures that "NULL" is displayed.
SELECT tv_shows.title, COALESCE(tv_genres.name, 'NULL') AS tv_genres_name
FROM tv_shows
LEFT JOIN tv_show_genre ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres_name ASC;
