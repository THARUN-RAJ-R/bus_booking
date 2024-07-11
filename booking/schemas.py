from pydantic import BaseModel
from fastapi import Form


class Booking(BaseModel):
    user_id: str
    route_id: int
    seat_number: int
