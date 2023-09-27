from dataclasses import dataclass

from environs import Env
from sqlalchemy import URL


@dataclass
class DatabaseConfig:
    url: URL


@dataclass
class RedisConfig:
    host: str
    port: int
    password: str


@dataclass
class TelegramBot:
    token: str
    admin_ids: list[int]
    write_logs: bool


@dataclass
class Miscellaneous:
    other_params: str = ''


@dataclass
class Config:
    bot: TelegramBot
    database: DatabaseConfig
    redis: RedisConfig
    misc: Miscellaneous


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        bot=TelegramBot(
            token=env.str('BOT_TOKEN'),
            admin_ids=list(map(int, env.list('ADMINS'))),
            write_logs=env.bool('WRITE_LOGS'),
        ),
        database=DatabaseConfig(
            url=URL.create(
                drivername='postgresql+asyncpg',
                username=env.str('POSTGRES_USER'),
                password=env.str('POSTGRES_PASSWORD'),
                host=env.str('POSTGRES_HOST'),
                port=env.int('POSTGRES_PORT'),
                database=env.str('POSTGRES_DB')
            )
        ),
        redis=RedisConfig(
            host=env.str('REDIS_HOST'),
            port=env.int('REDIS_PORT'),
            password=env.str('REDIS_PASSWORD')
        ),
        misc=Miscellaneous()
    )
