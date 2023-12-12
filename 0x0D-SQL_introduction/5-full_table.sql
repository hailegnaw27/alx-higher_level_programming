-- 5-full_table.sql

-- This script prints the full description of the table first_table from the specified database

SELECT TABLE_NAME, CREATE_TABLE
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = 'hbtn_0c_0'
AND TABLE_NAME = 'first_table';

