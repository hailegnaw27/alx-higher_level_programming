-- 12-no_cheating.sql

-- This script updates the score of Bob to 10 in the table second_table using the name field

UPDATE second_table
SET score = 10
WHERE name = 'Bob';
