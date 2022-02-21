from pyrogram import Client, filters
from pyrogram.types import Message
from plugins.neededshits.cust_p_filters import (
    Admin_Filter
)

@Client.on_message(
    filters.command(["pin"]) &
    Admin_Filter
)
async def pin(_, message: Message):
    if not message.reply_to_message:
        return
    await message.reply_to_message.pin()


@Client.on_message(
    filters.command(["unpin"]) &
    Admin_Filter
)
async def unpin(_, message: Message):
    if not message.reply_to_message:
        return
    await message.reply_to_message.unpin()
