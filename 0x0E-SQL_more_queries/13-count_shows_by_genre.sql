-- Displays all genres from the database hbtn_0d_tvshows along with the number of the server
-- shows linked to each on sever
-- Does not display genres without linked shows on server
-- Records are ordered by descending number of shows linked on server
SELECT g.`name` AS `genre`,
       COUNT(*) AS `number_of_shows`
  FROM `tv_genres` AS g
       INNER JOIN `tv_show_genres` AS t
       ON g.`id` = t.`genre_id`
 GROUP BY g.`name`
 ORDER BY `number_of_shows` DESC;
