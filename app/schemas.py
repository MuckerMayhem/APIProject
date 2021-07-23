from typing import List, Optional

from pydantic import BaseModel


class Configuration(BaseModel):
    id: int
    name: str
    config: str

    class Config:
        orm_mode = True