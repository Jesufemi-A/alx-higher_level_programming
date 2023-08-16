-- Displays all the cities inside CA in the database hbtn_0d_usa on my server
-- Results are ordered in ascending order of cities.id on my server
SELECT `id`, `name`
FROM `cities`
WHERE `state_id` IN
       (SELECT `id`
		FROM `states`
		WHERE `name` = "California")
ORDER BY `id`;
