from fastapi.routing import APIRouter
from .schemas import SmsReceiver

router = APIRouter()


@router.post("/sms")
async def sms_receiver(sms: SmsReceiver):
    print("-----------------")
    print(sms)
    print("-----------------")


@router.post("/push")
async def sms_receiver(sms: SmsReceiver):
    print("-----------------")
    print(sms)
    print("-----------------")
