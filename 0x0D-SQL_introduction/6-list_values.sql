--This is a script the lists all values in the table first_table from the database hbtn_0c_0 in your MySQL server.
mysql -h localhost -u username -p password $1 -e "SELECT * FROM first_table"