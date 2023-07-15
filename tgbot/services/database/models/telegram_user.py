from sqlalchemy import Column, BigInteger, DateTime
from sqlalchemy.sql.expression import text

from tgbot.services.database.base import Base


class TelegramUser(Base):
    __tablename__ = 'telegram_user'

    telegram_id = Column(BigInteger, primary_key=True, unique=True, autoincrement=False)
    created_at = Column(DateTime(), nullable=False, server_default=text('NOW()'))
