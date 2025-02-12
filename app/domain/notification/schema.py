from pydantic import BaseModel


class SmsRequest(BaseModel):
    sender: str
    message: str
    timestamp: int


class PushRequest(BaseModel):
    sender: str
    message: str
    timestamp: int