--This is a script to create a table in a database
mysql -h localhost -u root -p hbtn_0d_db -e "CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT, checked BOOLEAN); INSERT INTO second_table (id, name, score, checked) VALUES (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8);"
    