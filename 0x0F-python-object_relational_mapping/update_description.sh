#!/usr/bin/env bash

# A Bash script that writes the description of the database to a README file
rm hbtn_0e_6_usa_description.md
echo -e "\n\nThis README file contains a description of the hbtn_0e_6_usa database.\n\n" >> hbtn_0e_6_usa_description.md
./describe_hbtn_0e_4_usa.sh >> hbtn_0e_6_usa_description.md
echo ""
echo -e "\nCreated a file: hbtn_0e_6_usa_description.md\n"
echo "$ cat hbtn_0e_6_usa_description.md"
sleep 3
echo -e "\nRunning command...\n"
sleep 3
echo ""
cat hbtn_0e_6_usa_description.md
sleep 2
echo ""
echo -e "Command run!\n"
sleep 2
echo -e "Get back to work.\n"
