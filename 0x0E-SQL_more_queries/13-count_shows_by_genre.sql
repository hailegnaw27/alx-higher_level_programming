-- Script to count shows by genre
SELECT tv_show_genres.genre_id AS genre, COUNT(*) AS number_of_shows
FROM tv_show_genres
GROUP BY genre
ORDER BY number_of_shows DESC;

