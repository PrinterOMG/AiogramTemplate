import os

from dotenv import load_dotenv
from pydantic import BaseModel
from sqlalchemy import URL


class DatabaseConfig(BaseModel):
    url: str


class RedisConfig(BaseModel):
    host: str
    port: int
    password: str | None


class TelegramBot(BaseModel):
    token: str
    admin_ids: list[int]
    write_logs: bool


class Miscellaneous(BaseModel):
    other_params: str = ''


class Config(BaseModel):
    bot: TelegramBot
    database: DatabaseConfig
    redis: RedisConfig
    misc: Miscellaneous


def load_config(path: str = None):
    load_dotenv(dotenv_path=path)

    return Config(
        bot=TelegramBot(
            token=os.getenv('BOT_TOKEN'),
            admin_ids=os.getenv('ADMINS', '').split(','),
            write_logs=os.getenv('WRITE_LOGS', 'False'),
        ),
        database=DatabaseConfig(
            url=URL.create(
                drivername='postgresql+asyncpg',
                username=os.getenv('POSTGRES_USER'),
                password=os.getenv('POSTGRES_PASSWORD'),
                host=os.getenv('POSTGRES_HOST', '127.0.0.1'),
                port=os.getenv('POSTGRES_PORT', 5432),
                database=os.getenv('POSTGRES_DB')
            ).__str__()
        ),
        redis=RedisConfig(
            host=os.getenv('REDIS_HOST', '127.0.0.1'),
            port=os.getenv('REDIS_PORT', 6379),
            password=os.getenv('REDIS_PASSWORD')
        ),
        misc=Miscellaneous()
    )
