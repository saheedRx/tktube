from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Just Send Youtube Url(url only).\n\nExamples👇 ✅\nhttps://youtube.com/watch?v=xxxx \nhttps://youtu.be/xxxx\n\nDon't Send like this👇 ❌\nhttps://youtube.com/xxxx<b>?feature=share</b>\n(Remove unwanted text from your URL)\n\n\n@Tamil_Kingdom"
    await message.reply_text(helptxt)
