from typing import List

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.domain.user.model import Account
from app.domain.notification.model import SmsNotification, PushNotification


class Device(Base):
    __tablename__ = "device"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    token: Mapped[str]

    account_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    account: Mapped["Account"] = relationship(back_populates="devices")

    push_notifications: Mapped[List["PushNotification"]] = relationship(
        back_populates="device", cascade="all, delete-orphan"
    )
    sms_notifications: Mapped[List["SmsNotification"]] = relationship(
        back_populates="device", cascade="all, delete-orphan"
    )
