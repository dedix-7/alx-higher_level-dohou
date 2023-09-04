#!/usr/bin/bash

# A Bash script that describes the tables in the database hbtn_0e_4_usa
echo ""
echo "The database hbtn_0e_4_usa"
echo ""
echo "Describing the 'cities' table..."
echo "SELECT * FROM cities;" | mysql -hlocalhost -uroot -p hbtn_0e_4_usa
echo ""
echo "Describing the 'states' table"
echo "SELECT * FROM states;" | mysql -hlocalhost -uroot -p hbtn_0e_4_usa
echo ""
echo -e "To update the database README file, run this command:\n\n $ ./update_description.sh\n"
echo ""
