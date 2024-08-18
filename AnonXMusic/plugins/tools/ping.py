from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from AnonXMusic import app
from AnonXMusic.core.call import Anony
from AnonXMusic.utils import bot_sys_stats
from AnonXMusic.utils.decorators.language import language
from AnonXMusic.utils.inline import supp_markup
from config import BANNED_USERS, VIDEO_PATH  # Make sure to import VIDEO_PATH 

# Assuming VIDEO_PATH is defined correctly in your config.py
# VIDEO_PATH = "https://example.com/your_video.mp4" 


VIDEO_PATH = "https://graph.org/file/7fd7aa71aa57a235a8944.mp4"


@app.on_message(filters.command(["ping", "alive"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()

    # Send the video first 
    response = await message.reply_video(
        video=VIDEO_PATH,
        caption=_["ping_1"].format(app.mention),
    )
    
    pytgping = await Anony.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000

    await response.edit_caption( # Edit the video caption
        caption=_["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=supp_markup(_),
    )