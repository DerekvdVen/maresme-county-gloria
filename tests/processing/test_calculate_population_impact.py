from app.processing.calculate_population_impact import calculate_population_impact
from tests.conftest import example_files_path


def test_calculate_population_impact():
    n_people_affected = calculate_population_impact(
        population=example_files_path / "esp_pd_2020_1km.tif",
        flooding_areas=example_files_path / "flood_polygons.geojson",
    )
    assert n_people_affected > 0
