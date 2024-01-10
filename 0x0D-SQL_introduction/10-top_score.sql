-- 10-top_score.sql

-- This script lists all records of the table second_table, displaying both the score and the name, and ordering them by score (top first)

SELECT score, name
FROM second_table
ORDER BY score DESC;

