import json

from fastapi import APIRouter

from app.processing.calculate_affected_roads import calculate_affected_roads
from app.processing.calculate_flooding_area import (
    calculate_flooding_area_km2,
    map_flooding_area_to_geojson,
)
from app.processing.calculate_population_impact import calculate_population_impact

router = APIRouter()


@router.get("/flood_analytics")
async def get_flood_analytics() -> json:
    calculate_flooding_area_km2()

    calculate_affected_roads()

    calculate_population_impact()


@router.get("/flood_map")
async def get_flood_map() -> json:
    flood_map = map_flooding_area_to_geojson()
    return flood_map
