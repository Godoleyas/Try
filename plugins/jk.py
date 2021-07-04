from pyrogram import Client, Filters


@Client.on_message(Filters.command(["boni"]))
async def start(client, message):
    bonitxt = f"I have a question for you boni, Why ay u gay?"
    await message.reply_text(bonitxt)
    
    @Client.on_message(Filters.command(["boni is"]))
async def start(client, message):
    boniistxt = f"Gay"
    await message.reply_text(boniistxt)
    
    @Client.on_message(Filters.command(["Hey bot what's the smallest thing you have seen?"]))
async def start(client, message):
    natroasttxt = f"Nathan's brain"
    await message.reply_text(natroastxt)
    
    @Client.on_message(Filters.command(["@BekiKebe"]))
async def start(client, message):
    bekitxt = f"He is my nigga"
    await message.reply_text(bekitxt)


    
