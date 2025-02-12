from datetime import datetime

from sqlalchemy import ForeignKey, DateTime
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.domain.device.model import Device


class SmsNotification(Base):
    __tablename__ = "sms_notification"

    id: Mapped[int] = mapped_column(primary_key=True)
    sender: Mapped[str] = mapped_column(String)
    message: Mapped[str] = mapped_column(Text)
    time: Mapped[datetime] = mapped_column(DateTime)

    device_id: Mapped[int] = mapped_column(ForeignKey("device.id"))
    device: Mapped["Device"] = relationship(back_populates="sms_notifications")


class PushNotification(Base):
    __tablename__ = "push_notification"

    id: Mapped[int] = mapped_column(primary_key=True)
    sender: Mapped[str] = mapped_column(String)
    message: Mapped[str] = mapped_column(Text)
    time: Mapped[datetime] = mapped_column(DateTime)

    device_id: Mapped[int] = mapped_column(ForeignKey("device.id"))
    device: Mapped["Device"] = relationship(back_populates="push_notifications")
