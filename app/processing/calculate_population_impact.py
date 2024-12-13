from pathlib import Path

import geopandas as gpd
import rasterio
from rasterstats import zonal_stats


def filter_out_small_polygons(
    polygons: gpd.GeoDataFrame, polygon_size_filter: float = 8.786716496054427e-07
):
    only_large_polygons = polygons[polygons.geometry.area >= polygon_size_filter]
    return only_large_polygons.dissolve()


def calculate_population_impact(
    population: Path,
    flooding_areas: Path,
):
    with rasterio.open(population) as src:
        print(src.crs)

    polygons = gpd.read_file(flooding_areas)
    only_large_polygons = filter_out_small_polygons(polygons)

    stats = zonal_stats(
        only_large_polygons,
        population,
        all_touched=True,
        stats="count min mean max sum",
    )

    return stats[0]["sum"]
