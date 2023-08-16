-- Shows all cities in the database hbtn_0d_usa on my server
-- Records are sorted in ascending order of cities.id on my server
SELECT c.`id`, c.`name`, s.`name`
  FROM `cities` AS c
       INNER JOIN `states` AS s
       ON c.`state_id` = s.`id`
 ORDER BY c.`id`;
