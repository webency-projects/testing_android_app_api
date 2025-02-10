from pydantic import BaseModel
from typing import Optional


class SmsRequest(BaseModel):
    sender: str
    message: str
    timestamp: int


class PushRequest(BaseModel):
    sender: str
    message: str
    timestamp: int


class DeviceInfoRequest(BaseModel):
    deviceId: Optional[str] = None
    device: Optional[str] = None
    manufacturer: Optional[str] = None
    model: Optional[str] = None
    brand: Optional[str] = None
    versionRelease: Optional[str] = None
    sdkInt: Optional[int] = None
