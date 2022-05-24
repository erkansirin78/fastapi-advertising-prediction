from pydantic import BaseModel

class Advertising(BaseModel):
    TV: float
    Radio: float
    Newspaper: float

    class Config:
        schema_extra = {
            "example": {
                "TV": 230.1,
                "Radio": 37.8,
                "Newspaper": 69.2,
            }
        }
