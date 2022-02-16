#created by by @Arjun_La_Lis_A - tg
#use with proper credits

import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.neededshits.cust_p_filters import f_onw_fliter


PASSWORD_STRINGS = ("😂😂😂",
                    "😂😂😂🤣",
                   )
PICS1_PC = ("https://telegra.ph/file/6d5a7465f6ae6c2f6fb6b.jpg")


@Client.on_message(
    filters.command("/breakup", COMMAND_HAND_LER) &
    f_onw_fliter
)
async def breakup(_, message):
    """ /breakup strings """
    effective_string = random.choice(PASSWORD_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_photo(
            photo=(PICS1_PC),
            message.reply_to_message.reply_text(effective_string)
    else:
       message.reply_to_message:
        await message.reply_to_message.reply_photo(
            photo=(PICS1_PC),
            message.reply_to_message.reply_text(effective_string)
