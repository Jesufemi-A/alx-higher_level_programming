-- Displays all shows contained in the database hbtn_0d_tvshows from server
-- Displays NULL for shows without genres from my server
-- Records are ordered in ascending order of tv_shows.title and tv_show_genres.genre_id on my server
SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
       LEFT JOIN `tv_show_genres` AS g
       ON s.`id` = g.`show_id`
 ORDER BY s.`title`, g.`genre_id`;
