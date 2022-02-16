#created by by @Arjun_La_Lis_A - tg
#use with proper credits

import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.neededshits.cust_p_filters import f_onw_fliter


PASSWORD_STRINGS = (
    "Habeebi.. Come to dubai 😂😂 ",
    "Habeebi.. Come to dubai 😂😂",
)


@Client.on_message(
    filters.command("/breakup", COMMAND_HAND_LER) &
    f_onw_fliter
)
async def password(_, message):
    """ /breakup strings """
    effective_string = random.choice(PASSWORD_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)
