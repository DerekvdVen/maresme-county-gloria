from fastapi.testclient import TestClient

from app.main import app
from tests.conftest import example_files_path

client = TestClient(app)


def test_post_flood_analytics():
    payload = {
        "before": str(example_files_path / "Before_Flood.tif"),
        "after": str(example_files_path / "After_Flood.tif"),
        "threshold": 0.5,
        "pixel_size_m": 30,
        "flooding_areas": str(example_files_path / "flood_polygons.geojson"),
        "roads": str(example_files_path / "roads.geojson"),
        "population": str(example_files_path / "esp_pd_2020_1km.tif"),
    }

    response = client.post("/flood_analytics", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert "flooding_area_km2" in data
    assert "road_impact_m" in data
    assert "population_impact" in data


def test_get_flood_map():
    params = {
        "before": example_files_path / "After_Flood.tif",
        "after": example_files_path / "After_Flood.tif",
        "threshold": 0.5,
    }

    response = client.get("/flood_map", params=params)

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
