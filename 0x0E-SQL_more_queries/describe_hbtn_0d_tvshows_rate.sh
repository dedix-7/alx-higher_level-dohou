#!/usr/bin/env bash

# A Bash script that describes everything about the hbtn_0d_tvshows_rate database

echo ""
echo "Showing tables in the database hbtn_0d_tvshows_rate database" ; echo "" ; echo 'SHOW TABLES;' | mysql -hlocalhost -uroot -p hbtn_0d_tvshows_rate
echo ""
echo "tv_genres - Description" ; echo 'SELECT * FROM tv_genres;' | mysql -hlocalhost -uroot -p hbtn_0d_tvshows_rate
echo ""
echo "tv_show_genres - Description" ; echo 'SELECT * FROM tv_show_genres;' | mysql -hlocalhost -uroot -p hbtn_0d_tvshows_rate
echo ""
echo "tv_shows - Description" ; echo 'SELECT * FROM tv_shows;' | mysql -hlocalhost -uroot -p hbtn_0d_tvshows_rate
echo ""
echo "tv_shows_ratings - Description" ; echo 'SELECT * FROM tv_show_ratings;' | mysql -hlocalhost -uroot -p hbtn_0d_tvshows_rate
echo ""
