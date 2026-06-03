from typing import Any
from pydantic import BaseModel
class FanData(BaseModel):
    SLOW = 1
    MEDIUM = 2
    FAST = 3
    speed: int = SLOW
    on: bool = False
    radius: float = 5
    color: str = "blue"

class ReturnValueSchema(BaseModel):
    is_success : bool
    value: Any
    message: str