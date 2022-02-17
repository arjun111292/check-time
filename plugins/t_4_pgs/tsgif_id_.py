from pyrogram import Client, filters

# Gif ID 
@Client.on_message(filters.command(["gifid"]))
async def gifid(bot, message):   
    if message.reply_to_message.gif:
       await message.reply(f"**Gif ID is**  \n `{message.reply_to_message.gif.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.gif.file_unique_id}`", quote=True)
    else: 
       await message.reply("Not a Gif file🥱")
