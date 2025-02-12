from pydantic import BaseModel
from typing import Optional


class DeviceInfoRequest(BaseModel):
    androidId: Optional[str] = None
    device: Optional[str] = None
    manufacturer: Optional[str] = None
    model: Optional[str] = None
    brand: Optional[str] = None
    versionRelease: Optional[str] = None
    sdkInt: Optional[int] = None