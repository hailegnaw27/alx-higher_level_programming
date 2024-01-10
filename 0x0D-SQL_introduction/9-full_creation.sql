-- 9-full_creation.sql

-- This script creates a table second_table and adds multiple rows with the given data

CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

INSERT INTO second_table (id, name, score)
VALUES (1, 'John', 10),
       (2, 'Alex', 3),
       (3, 'Bob', 14),
       (4, 'George', 8);

