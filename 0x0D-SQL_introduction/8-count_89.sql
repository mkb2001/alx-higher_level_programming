--This is  a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.
mysql -h localhost -u username -p password hbtn_0c_0 -e "SELECT COUNT(*) FROM first_table WHERE id = 89;"
 