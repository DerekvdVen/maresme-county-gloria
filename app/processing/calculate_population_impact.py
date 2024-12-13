from pathlib import Path

import geopandas as gpd
import rasterio
from rasterstats import zonal_stats


def calculate_population_impact(
    population: Path,
    flooding_areas: Path,
    polygon_size_filter: float = 8.786716496054427e-07,
):
    with rasterio.open(population) as src:
        print(src.crs)

    polygons = gpd.read_file(flooding_areas)
    large_polygons = polygons[polygons.geometry.area >= polygon_size_filter]

    large_polygons = large_polygons.dissolve()

    stats = zonal_stats(
        large_polygons, population, all_touched=True, stats="count min mean max sum"
    )

    return stats[0]["sum"]
