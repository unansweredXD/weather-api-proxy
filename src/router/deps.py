from typing import Annotated

from fastapi.params import Query

CityList = Annotated[list[str], Query()]
