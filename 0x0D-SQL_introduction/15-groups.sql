-- This is a script that groups the number of rows in the table second_table by score and orders the result by the number of rows in descending order.
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
