from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("⚜Our Channel⚜", url="https://t.me/Tamil_Kingdom")],
        [InlineKeyboardButton("🃏Admins🃏", url="https://t.me/TamilKingdomAdmin_Bot")]
    ])
    welcomed = f"வணக்கம் <b>{message.from_user.first_name}</b>\n\n\nஉதவிக்கு 👉 /help"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
