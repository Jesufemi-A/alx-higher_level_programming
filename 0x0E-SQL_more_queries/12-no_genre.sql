-- Displays all shows in the database hbtn_0d_tvshows without any genre linked on my server
-- Records are arranged in ascending order of tv_shows.title and tv_show_genres.genre_id on my server
SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
       LEFT JOIN `tv_show_genres` AS g
       ON s.`id` = g.`show_id`
       WHERE g.`genre_id` IS NULL
 ORDER BY s.`title`, g.`genre_id`;
