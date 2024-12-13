from pathlib import Path
from typing import Dict

from fastapi import APIRouter, Query
from pydantic import BaseModel

from app.processing.calculate_affected_roads import calculate_road_impact_m
from app.processing.calculate_flooding_area import (
    calculate_flooding_area_km2,
    map_flooding_area_to_geojson,
)
from app.processing.calculate_population_impact import calculate_population_impact

router = APIRouter()


class FloodAnalyticsRequest(BaseModel):
    before: str
    after: str
    threshold: float
    pixel_size_m: int
    flooding_areas: str
    roads: str
    population: str


# Use a pydantic model with a post request because there are a lot of inputs needed
@router.post("/flood_analytics")
async def get_flood_analytics(request: FloodAnalyticsRequest):
    before = request.before
    after = request.after
    threshold = request.threshold
    pixel_size_m = request.pixel_size_m
    flooding_areas = request.flooding_areas
    roads = request.roads
    population = request.population

    flooding_area_km2 = calculate_flooding_area_km2(
        before=Path(before),
        after=Path(after),
        threshold=threshold,
        pixel_size_m=pixel_size_m,
    )
    road_impact_m = calculate_road_impact_m(
        flooding_areas=Path(flooding_areas), roads=Path(roads)
    )
    population_impact = calculate_population_impact(
        flooding_areas=Path(flooding_areas), population=Path(population)
    )

    return {
        "flooding_area_km2": flooding_area_km2,
        "road_impact_m": road_impact_m,
        "population_impact": population_impact,
    }


# Use query params as there are ony a few inputs
# GET /flood_map?before=path/to/before_raster.tif&after=path/to/after_raster.tif&threshold=0.5&pixel_size=30
@router.get("/flood_map")
async def get_flood_map(
    before: str = Query(..., description="Path to the before raster file"),
    after: str = Query(..., description="Path to the after raster file"),
    threshold: float = Query(..., description="Threshold value for flooding analysis"),
) -> Dict:
    flood_map = map_flooding_area_to_geojson(
        before=Path(before), after=Path(after), threshold=threshold
    )
    return flood_map
