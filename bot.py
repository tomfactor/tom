from pyrogram import Client, idle
from pyromod import listen



bot = Client(
    "mo",
    api_id=9157919,
    api_hash="b90c282e584222babde5f68b5b63ee3b",
    bot_token="5671865882:AAFMpMUYPvexNnT2HIsgaIYxeQTWWcWdSec",
    plugins=dict(root="Maker")
    )

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    UU_X9 = "DEV_TOM"
    await bot.send_message(UU_X9, "**تم تشغيل الصانع بنجاح ...🚦**")
    await idle()
