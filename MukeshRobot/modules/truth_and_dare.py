import random

from telegram import Update
from telegram.ext import CallbackContext

import MukeshRobot.modules.truth_and_dare_string as truth_and_dare_string
from MukeshRobot import dispatcher
from MukeshRobot.modules.disable import DisableAbleCommandHandler


def truth(update: Update, context: CallbackContext):
    context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.TRUTH))


def dare(update: Update, context: CallbackContext):
    context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.DARE))


TRUTH_HANDLER = DisableAbleCommandHandler("truth", truth)
DARE_HANDLER = DisableAbleCommandHandler("dare", dare)

dispatcher.add_handler(TRUTH_HANDLER)
dispatcher.add_handler(DARE_HANDLER)

__help__ = """
*ᴛʀᴜᴛʜ & ᴅᴀʀᴇ*
 ❍ /truth  *:* sᴇɴᴅs ᴀ ʀᴀɴᴅᴏᴍ ᴛʀᴜᴛʜ sᴛʀɪɴɢ.
 ❍ /dare  *:* sᴇɴᴅs ᴀ ʀᴀɴᴅᴏᴍ ᴅᴀʀᴇ sᴛʀɪɴɢ.

𝘽𝙮 [𓆩｡</𝙌> ｡𓆪 #𝙇𝙚𝙨𝙨𝘼𝙘𝙩𝙞𝙫𝙚](https://t.me/@AnDrOiiiDUsEr)
"""
__mod_name__ = "⚡ꜰᴜɴ⚡"