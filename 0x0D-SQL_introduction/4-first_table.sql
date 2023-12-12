-- 4-first_table.sql

-- This script creates a table called first_table in the specified database

USE dbname;

CREATE TABLE IF NOT EXISTS first_table (
  id INT,
  name VARCHAR(256)
);

