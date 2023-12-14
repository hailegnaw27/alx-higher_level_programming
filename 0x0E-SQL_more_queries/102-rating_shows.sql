-- Script to list shows by rating
SELECT tv_shows.title, SUM(tv_shows_rate.rating) AS rating_sum
FROM tv_shows
JOIN tv_shows_rate ON tv_shows.id = tv_shows_rate.show_id
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;

