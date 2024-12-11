import json

from fastapi import APIRouter

from app.processing.calculate_affected_roads import calculate_affected_roads
from app.processing.calculate_flooding_area import calculate_flooding_area, map_flooding_area
from app.processing.calculate_population_impact import calculate_population_impact

router = APIRouter()


@router.get("/flood_analytics")
async def get_flood_analytics():
    calculate_affected_roads()
    calculate_flooding_area()
    calculate_population_impact()


@router.get("/flood_map")
async def get_flood_map():
    map_flooding_area()
