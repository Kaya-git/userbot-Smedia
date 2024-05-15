from pyrogram import Client
from config import conf


app = Client(
    name='Smedia', api_id=conf.botconf.api_id, api_hash=conf.botconf.api_hash
)


app.run()
