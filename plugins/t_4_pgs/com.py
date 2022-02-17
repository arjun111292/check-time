#created by by @Arjun_La_Lis_A - tg
#use with proper credits

import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.neededshits.cust_p_filters import f_onw_fliter


COMEDY_STRINGS = (
    "CAACAgUAAxkBAAIDTWIN7t5h_8P6FDH-fkeliFYtuTSoAAJaBAAC78rxVyVXsqnnB2vXHgQ, CAACAgUAAxkBAAIDTWIN7t5h_8P6FDH-fkeliFYtuTSoAAJaBAAC78rxVyVXsqnnB2vXHgQ",
    "CAACAgUAAxkBAAIDTWIN7t5h_8P6FDH-fkeliFYtuTSoAAJaBAAC78rxVyVXsqnnB2vXHgQ",
    "CAACAgUAAxkBAAIDTWIN7t5h_8P6FDH-fkeliFYtuTSoAAJaBAAC78rxVyVXsqnnB2vXHgQ", 
)


@Client.on_message(
    filters.command("comedy", COMMAND_HAND_LER) &
    f_onw_fliter
)
async def comedy(_, message):
    """ /comedy strings """
    effective_string = random.choice(COMEDY_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_sticker(effective_string)
    else:
        await message.reply_sticker(effective_string)
