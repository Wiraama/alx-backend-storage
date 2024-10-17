-- some shit
SELECT band_name, (IFFULL(split, 2022) - formed)
AS lifespan FROM metal_bands WHERE main_style LIKE '%Glam rock%' ORDER BY lifespan DESC;
