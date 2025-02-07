from pydantic import BaseModel


class SmsReceiver(BaseModel):
    address: str
    message: str