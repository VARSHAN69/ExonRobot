from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import __version__ as o
from telethon import __version__ as s

from Exon import app as pbot

ABISHNOIX = "https://te.legra.ph/file/7ad64153b3cf829acf0c9.jpg"


@pbot.on_message(filters.command(["repo", "source"]))
async def repo(_, message):
    await message.reply_photo(
        photo=ABISHNOIX,
        caption=f"""✨ **ʜᴇʏ {message.from_user.mention},**

**ʀᴇᴘᴏ ᴏᴡɴᴇʀ  : [ᴀɪᴢᴇɴ](https://t.me/Aizenff)**
**ᴘʏᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ :** `{y()}`
**ʟɪʙʀᴀʀʏ ᴠᴇʀꜱɪᴏɴ :** `{o}`
**ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ :** `{s}`
**ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀꜱɪᴏɴ :** `{z}`
**ʙᴏᴛ ᴠᴇʀꜱɪᴏɴ :** `2.69`
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•ɢʀᴏᴜᴘ•", url="https://t.me/INDIAN_HACKER_GROUP"
                    ),
                    InlineKeyboardButton(
                        "•ʀᴏʙᴏᴛ•", url="https://t.me/indianhackerz_management_robot"
                    ),
                ]
            ]
        ),
    )
