from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class Configuration(BaseModel):
    id: int
    name: str
    config: str

    class Config:
        orm_mode = True


class Fish(BaseModel):
    date: datetime
    facility_ref_number: int
    licence_holder: str
    site_name: str
    fish_health_zone: float

    class Config:
        orm_mode = True
