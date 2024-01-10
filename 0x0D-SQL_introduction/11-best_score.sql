-- 11-best_score.sql

-- This script lists all records from the table second_table with a score >= 10, displaying both the score and the name, and ordering them by score (top first)

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
