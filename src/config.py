import os
from dotenv import load_dotenv
from dataclasses import dataclass


load_dotenv()


@dataclass
class User:
    user_hash = {}


@dataclass
class BotConf:
    api_hash = os.environ.get("API_HASH")
    api_id = os.environ.get("API_ID")


@dataclass
class RedisConfig:
    """ Redis connection variables"""

    db: str = int(os.environ.get("REDIS_DATABASE", 1))
    host: str = os.environ.get("REDIS_HOST")
    port: str = os.environ.get("REDIS_PORT")
    state_ttl: int = os.environ.get("REDIS_TTL_STATE", None)
    data_ttl: int = os.environ.get("REDIS_TTL_DATA", None)


@dataclass
class Config:
    timetable = {}

    message_table = {
        "1": ["Текст1", 6],
        "2": ["Текст2", 39],
        "3": ["Текст3", 1560]
    }

    message_queue = []

    botconf = BotConf()
    user = User()


conf = Config()
