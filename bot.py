from pyrogram import Client, idle
from pyromod import listen



bot = Client(
    "mo",
    api_id=8186557,
    api_hash="efd77b34c69c164ce158037ff5a0d117",
    bot_token="6267386255:AAFUAJ8emYpsKd7TWl9v_ugy_40lGFlDHfU",
    plugins=dict(root="Maker")
    )

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    UU_X9 = "MohamedHelal_l"
    await bot.send_message(UU_X9, "**تم تشغيل الصانع بنجاح ...🚦**")
    await idle()
