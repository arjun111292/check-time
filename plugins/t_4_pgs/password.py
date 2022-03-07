#created by by @Arjun_La_Lis_A - tg
#use with proper credits
# andhada mwona pear ayo 🤞🏻🙂
import string
import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.neededshits.cust_p_filters import f_onw_fliter

"""
poolishness 🐧
PASSWORD_STRINGS = (
    "പാസ്‌വേഡ് ഉണ്ടാക്കാൻ എനിക്കറിയില്ല🙄",
    "പാസ്‌വേഡ് ഉണ്ടാക്കാൻ എനിക്കറിയില്ല🙄..",
    "പാസ്‌വേഡ് ഉണ്ടാക്കാൻ എനിക്കറിയില്ല😫", 
)
"""

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def passw (leng):
  length = int(leng)
  random.shuffle(characters)
  pas = []
  for i in range (length):
    pas.append(random.choice(characters))
  random.shuffle(pas)
  return "".join(pas)

@Client.on_message(
    filters.command("password", COMMAND_HAND_LER) &
    f_onw_fliter
)
async def password(_, message):
    """ /password strings """
    effective_string = passw(20)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)
