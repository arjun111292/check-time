from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters


@Client.on_message(filters.photo & filters.private)
async def photo(client: Client, message: Message):
    try:
        await client.send_message(
            chat_id=message.chat.id,
            text="Select your required mode from below!ㅤㅤ",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="вяιgнт", callback_data="bright"),
                        InlineKeyboardButton(text="мιχє∂", callback_data="mix"),
                        InlineKeyboardButton(text="в & ω", callback_data="b|w"),
                    ],
                    [
                        InlineKeyboardButton(text="¢ιя¢ℓє", callback_data="circle"),
                        InlineKeyboardButton(text="вℓυя", callback_data="blur"),
                        InlineKeyboardButton(text="вσя∂єя", callback_data="border"),
                    ],
                    [
                        InlineKeyboardButton(text="ѕтι¢кєя", callback_data="stick"),
                        InlineKeyboardButton(text="яσтαтє", callback_data="rotate"),
                        InlineKeyboardButton(text="¢σитяαѕт", callback_data="contrast"),
                    ],
                    [
                        InlineKeyboardButton(text="ѕєρια", callback_data="sepia"),
                        InlineKeyboardButton(text="ρєи¢ιℓ", callback_data="pencil"),
                        InlineKeyboardButton(text="¢αятσσи", callback_data="cartoon"),
                    ],
                    [
                        InlineKeyboardButton(text="ιиνєят", callback_data="inverted"),
                        InlineKeyboardButton(text="¢ℓιρ", callback_data="glitch"),
                        InlineKeyboardButton(
                            text="яємσνє вg", callback_data="removebg"
                        ),
                    ],
                    [
                        InlineKeyboardButton(text="¢ℓσѕє", callback_data="close_data"),
                    ],
                ]
            ),
            reply_to_message_id=message.message_id,
        )
    except Exception as e:
        print("photomarkup error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_text("Something went wrong!", quote=True)
            except Exception:
                return
