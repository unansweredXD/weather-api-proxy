from typing import Optional

from pydantic import BaseModel


class ParametersResponse(BaseModel):
    temperature: Optional[float] = None
    feels: Optional[float] = None
    wind: Optional[dict] = None
    visibility: Optional[int] = None
    humidity: Optional[int] = None
