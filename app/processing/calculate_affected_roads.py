from pathlib import Path

import geopandas as gpd


def calculate_road_impact_m(
    roads: Path,
    flooding_areas: Path,
    polygon_size_filter: float = 8.786716496054427e-07,
) -> int:
    roads_gdf = gpd.read_file(roads)
    flooding_gdf = gpd.read_file(flooding_areas)

    large_flooding = flooding_gdf[flooding_gdf.geometry.area >= polygon_size_filter]
    large_flooding = large_flooding.dissolve()
    affected_roads = roads_gdf[
        roads_gdf.geometry.intersects(large_flooding.geometry.unary_union)
    ]

    affected_roads = affected_roads.to_crs(epsg=32631)

    affected_roads["length"] = affected_roads.geometry.length
    total_affected_length_m = affected_roads["length"].sum()

    return total_affected_length_m
