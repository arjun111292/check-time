from pyrogram import Client, filters
from pyrogram.types import Message
from plugins.neededshits.cust_p_filters import (
    admin_filter_f
)

@Client.on_message(
    filters.command(["pin"]) &
    admin_filter_f
)
async def pin(_, message: Message):
    if not message.reply_to_message:
        return
    await message.reply_to_message.pin()


@Client.on_message(
    filters.command(["unpin"]) &
    admin_filter_f
)
async def unpin(_, message: Message):
    if not message.reply_to_message:
        return
    await message.reply_to_message.unpin()
