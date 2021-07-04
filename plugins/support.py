from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["support"]), group=-2)
async def start(client, message):
    # return
    socialButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Youtube", url="https://t.me/PapyProjects")],
        [InlineKeyboardButton(
            "Tiktok", url="https://t.me/PapyProjectsbot")]
    ])
    huh = f"Subscribe to my Youtube and Tiktok account"
    await message.reply_text(huh, reply_markup=socialButton)
    raise StopPropagation
