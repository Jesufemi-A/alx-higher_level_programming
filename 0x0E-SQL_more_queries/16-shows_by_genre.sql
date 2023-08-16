-- Displays all shows and genres linked to the show from the on my server
-- database hbtn_0d_tvshows on my server
-- Records are arranged in ascending order of show titles and genre name on my server.
SELECT t.`title`, g.`name`
  FROM `tv_shows` AS t
       LEFT JOIN `tv_show_genres` AS s
       ON t.`id` = s.`show_id`

       LEFT JOIN `tv_genres` AS g
       ON s.`genre_id` = g.`id`
 ORDER BY t.`title`, g.`name`;
