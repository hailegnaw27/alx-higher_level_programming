-- 13-change_class.sql

-- This script removes all records with a score <= 5 from the table second_table

DELETE FROM second_table
WHERE score <= 5;
