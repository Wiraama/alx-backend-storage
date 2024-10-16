-- SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans
CREATE VIEW ranked_band_origins AS
SELECT
	origin,
	SUM(nb_fans) AS total_fans
FROM
	bands
GROUP BY
	origin
ORDER BY
	total_fans DESC;

-- see ranked list
SELECT
	origin,
	total_fans AS nb_fans
FROM
	ranked_band_origins;
