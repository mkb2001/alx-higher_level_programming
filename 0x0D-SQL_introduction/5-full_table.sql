-- This is  a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.
SELECT 
  COLUMN_NAME, 
  DATA_TYPE, 
  CHARACTER_MAXIMUM_LENGTH, 
  NUMERIC_PRECISION, 
  NUMERIC_SCALE, 
  COLUMN_DEFAULT, 
  IS_NULLABLE, 
  COLUMN_KEY, 
  EXTRA
FROM 
  INFORMATION_SCHEMA.COLUMNS 
WHERE 
  TABLE_NAME = 'first_table' 
AND 
  TABLE_SCHEMA = '$DB_NAME';
