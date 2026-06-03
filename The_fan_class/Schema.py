from typing import Any
from pydantic import BaseModel
SLOW = 1
MEDIUM = 2
FAST = 3
class FanData(BaseModel):
    
    speed: int = SLOW
    on: bool = False
    radius: float = 5.0
    color: str = "blue"

class ReturnValueSchema(BaseModel):
    is_success : bool
    value: Any
    message: str | None = None