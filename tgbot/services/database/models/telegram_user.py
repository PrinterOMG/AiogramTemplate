import datetime

from sqlalchemy import BigInteger, func
from sqlalchemy.orm import mapped_column, Mapped

from tgbot.services.database.base import Base


class TelegramUser(Base):
    __tablename__ = 'telegram_user'

    telegram_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, unique=True, autoincrement=False)
    created_at: Mapped[datetime.datetime] = mapped_column(nullable=False, server_default=func.now())
