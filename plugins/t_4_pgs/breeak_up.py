#created by by @Arjun_La_Lis_A - tg
#use with proper credits
  
import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.neededshits.cust_p_filters import f_onw_fliter


BREAK_STRINGS = (
    "<spoiler>Habeebi.. Come to dubai 😂😂😂..</spoiler>",
    "<spoiler>Habeebi.. Come to dubai 😂😂😂.</spoiler>",
    "<spoiler>Habeebi...Come to dubaii 😂😂😂😂..</spoiler>", 
)


@Client.on_message(
    filters.command("breakup", COMMAND_HAND_LER) &
    f_onw_fliter
)
async def breakup(_, message):
    """ /breakup strings """
    effective_string = random.choice(BREAK_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)
