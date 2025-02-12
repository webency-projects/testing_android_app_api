from pydantic import BaseModel
from typing import Optional


class UserRequest(BaseModel):
    email: str
    password: str
