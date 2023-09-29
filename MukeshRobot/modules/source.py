from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import __version__ as o
from telethon import __version__ as s

from MukeshRobot import OWNER_ID, dispatcher
from MukeshRobot import pbot as client

Mukesh = "https://graph.org/file/d874fc40ddf9ead0cad6b.jpg"


@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=Mukesh,
        caption=f"""**ʜᴇʏ​ {message.from_user.mention()},\n\nɪ ᴀᴍ [{dispatcher.bot.first_name}](t.me/{dispatcher.bot.username})**

:•||•●┼┼──🦋🖤 ⃝⃪⃕🥀

 ♨️ 𝘽𝙮 𓆩｡</𝙌> ｡𓆪 #𝙇𝙚𝙨𝙨𝘼𝙘𝙩𝙞𝙫𝙚 ♨️
    
              •||•●┼┼──🌸͜͡🌿─̶̶⃛͢⃝🍃卄

**[𓆩｡</𝙌> ｡𓆪 #𝙂𝘾𝙈𝙖𝙣𝙖𝙜𝙚𝙧](t.me/{dispatcher.bot.username}) sᴏᴜʀᴄᴇ ɪs ɴᴏᴡ ᴩᴜʙʟɪᴄ ᴀɴᴅ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📍ᴏᴡɴᴇʀ📍",f"tg://user?id={OWNER_ID}"
                    ),
                    InlineKeyboardButton(
                        "📍ʀᴇᴘᴏ📍",
                        url="https://github.com/",
                    ),
                ]
            ]
        ),
    )


__mod_name__ = "⚡Rᴇᴩᴏ⚡"
_help__ = """
 /repo  ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ 
 /source ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ
 
𝘽𝙮 [𓆩｡</𝙌> ｡𓆪 #𝙇𝙚𝙨𝙨𝘼𝙘𝙩𝙞𝙫𝙚](https://t.me/@AnDrOiiiDUsEr)
"""
