from fastapi import APIRouter
from fastapi_cache.decorator import cache

import settings
from router.deps import CityList
from schemas.weather import WeatherResponse, WeatherListResponse
from services.weather import WeatherService

router = APIRouter()


@router.get('/city', response_model=WeatherResponse)
@cache(expire=settings.CACHE_TTL)
async def get_city_weather(
        city: str,
        parameters: str
):
    return WeatherService().get_city_weather(city, parameters)


@router.get('/cities', response_model=WeatherListResponse)
@cache(expire=settings.CACHE_TTL)
async def get_city_list_weather(
        parameters: str,
        cities: CityList
):
    return WeatherService().get_city_list_weather(cities, parameters)
