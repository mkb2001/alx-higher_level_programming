-- This is a script that creates a table called unique_id with two columns: id and name. The id column should have a default value of 1 and should be unique.
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
