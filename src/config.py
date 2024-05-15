import os
from dotenv import load_dotenv

load_dotenv()


class BotConf:
    api_hash = os.environ.get("API_HASH")
    api_id = os.environ.get("API_ID")


class Config:
    botconf = BotConf()


conf = Config()
