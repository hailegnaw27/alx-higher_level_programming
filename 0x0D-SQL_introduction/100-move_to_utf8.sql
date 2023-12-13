-- 100-move_to_utf8.sql

-- This script converts the hbtn_0c_0 database to UTF8

-- Convert the database to UTF8
USE 'hbtn_0c_0'

-- Convert the table to UTF8
ALTER TABLE 'first_table'

-- Convert the field to UTF8
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
