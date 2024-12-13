from pathlib import Path

import numpy as np
import rasterio
from rasterio.features import shapes


def calculate_flooding_area_km2(
    before: Path, after: Path, threshold: float = 1, pixel_size_m: int = 30
) -> float:
    with rasterio.open(before) as before_src, rasterio.open(after) as after_src:
        before_data = before_src.read(1)
        after_data = after_src.read(1)

    difference = before_data - after_data
    flooding_mask = difference > threshold

    flooded_area_pixels = np.sum(flooding_mask)

    pixel_area_km2 = (pixel_size_m**2) / 1_000_000  # Convert m2 to km2

    total_area_km2 = flooded_area_pixels * pixel_area_km2

    return total_area_km2


def map_flooding_area_to_geojson(before: Path, after: Path, threshold: float = 1):
    with rasterio.open(before) as before_src, rasterio.open(after) as after_src:
        before_data = before_src.read(1)
        after_data = after_src.read(1)
        transform = before_src.transform

    difference = before_data - after_data
    flooding_mask = difference > threshold

    shapes_generator = shapes(flooding_mask.astype(np.uint8), transform=transform)

    geometries = [
        {"type": "Feature", "geometry": shape, "properties": {"flooded": value}}
        for shape, value in shapes_generator
        if value == 1
    ]

    geojson = {"type": "FeatureCollection", "features": geometries}
    return geojson
