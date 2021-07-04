from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Contact @PapyProjectsBot for help I will see it 😁"
    await message.reply_text(helptxt)
