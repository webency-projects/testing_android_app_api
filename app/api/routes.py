from fastapi.routing import APIRouter
from .schemas import SmsRequest, PushRequest, DeviceInfoRequest

router = APIRouter()


@router.post("/sms")
async def sms_receiver(sms: SmsRequest):
    print("-----------------")
    print(sms)
    print("-----------------")


@router.post("/push")
async def push_receiver(push: PushRequest):
    print("-----------------")
    print(push)
    print("-----------------")


@router.post("/device")
async def device_info(device: DeviceInfoRequest):
    print("-----------------")
    print(device)
    print("-----------------")
