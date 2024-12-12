import json

import geopandas as gpd
import numpy as np

from app.processing.calculate_flooding_area import (
    calculate_flooding_area_km2,
    map_flooding_area_to_geojson,
)
from tests.conftest import example_files_path


def test_calculate_flooding_area():
    result = calculate_flooding_area_km2(
        before=example_files_path / "Before_Flood.tif",
        after=example_files_path / "After_Flood.tif",
    )
    assert type(result) == np.float64
    assert result > 0


def test_map_flooding_area():
    result = map_flooding_area_to_geojson(
        before=example_files_path / "Before_Flood.tif",
        after=example_files_path / "After_Flood.tif",
    )

    geo_df = gpd.read_file(json.dumps(result))
    assert all(geo_df.is_valid)
