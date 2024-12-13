from app.processing.calculate_affected_roads import calculate_road_impact_m
from tests.conftest import example_files_path


def test_calculate_road_impact():
    length_of_affected_roads_m = calculate_road_impact_m(
        roads=example_files_path / "roads.geojson",
        flooding_areas=example_files_path / "flood_polygons.geojson",
    )
    assert length_of_affected_roads_m > 0
