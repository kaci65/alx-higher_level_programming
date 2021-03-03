-- lists all cities of California that can be found in database hbtn_0d_usa
SELECT id, name
FROM cities
WHERE state.id = (
	SELECT id
	FROM states
	WHERE name = "California"
);
ORDER BY cities.id