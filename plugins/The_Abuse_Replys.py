#created by by @Arjun_La_Lis_A - tg
#use with proper credits

import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.neededshits.cust_p_filters import f_onw_fliter


AUNTYCX9_STRINGS = (
    "ശിവ ശിവ !!😐😐...ഡാ മോനേ, ഇവ നല്ല ശീലങ്ങളല്ല🔞🔞.......",
    "ശിവ ശിവ !!😐😐...ഡാ മോനേ, ഇവ നല്ല ശീലങ്ങളല്ല🔞🔞......", 
)


@Client.on_message(
    filters.command("abuse","myre","theri","fuck" COMMAND_HAND_LER) &
    f_onw_fliter
)
async def aunty(_, message):
    """ /abuse, myre, theri, fuck strings """
    effective_string = random.choice(AUNTYCX9)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)
