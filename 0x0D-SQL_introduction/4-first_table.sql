--This is a script that creates a table in a database
--The database name will be passed as an argument of mysql command
CREATE TABLE IF NOT EXISTS first_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
