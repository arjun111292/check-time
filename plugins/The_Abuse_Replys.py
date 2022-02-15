#created by by @Arjun_La_Lis_A - tg
#use with proper credits

import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.neededshits.cust_p_filters import f_onw_fliter


AUNTY_STRINGS = (
    "ഡാ നിന്റെ ഒക്കെ അമ്മയ്ക്കും പെങ്ങക്കും ഉള്ളതൊക്കെ തന്നാട എല്ലാർക്കും ഒള്ളത്..",
    "നിന്നെ കൊണ്ട് നാട്ടുകാർക്കും ഗുണോല്ല്യ വിട്ടുകാർക്കും ഗുണോല്ല്യ എന്തിനാ ഇങ്ങനെ നാണം കേട്ടു ജീവിക്കുന്നട പാട് വാഴെ ചെങ്കതളി വാഴ .", 
)


@Client.on_message(
    filters.command("aunty", COMMAND_HAND_LER) &
    f_onw_fliter
)
async def aunty(_, message):
    """ /aunty strings """
    effective_string = random.choice(AUNTY_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)
