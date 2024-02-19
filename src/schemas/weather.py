from typing import Optional, List

from pydantic import BaseModel

from schemas.parameters import ParametersResponse


class WeatherResponse(BaseModel):
    city_name: str
    parameters: Optional[ParametersResponse] = None


class WeatherListResponse(BaseModel):
    weather_list: List[WeatherResponse]
