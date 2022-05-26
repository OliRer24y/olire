from pyrogram import filters
from pyrogram.errors import UserAlreadyParticipant
import asyncio
from config import SUDO_USERS
from pyrogram.types import Message
from io import BytesIO, StringIO
from Zaid.main import Test, bot as Client

@Client.on_message(filters.command(["gcast", "broadcast"]))
async def bye(client, message):
    if message.from_user.id in SUDO_USERS:
        lol = await message.reply("`Globally Broadcasting Msg...`")
        if not message.reply_to_message:
            await lol.edit("Usage: /gcast for bot\n /agcast broadcast By assistant\n\n**Reply to any text message for gcast**")
            return
        msg = message.reply_to_message.text
        sent=0
        failed=0
        for dialog in client.iter_dialogs():
            try:
                await client.send_message(dialog.chat.id, msg)
                sent += 1
                await lol.edit(f"**Successfully Send Message To** `{sent}` **Group, Failed to Send Message To** `{failed}` **Group**")
            except:
                failed += 1
                await lol.edit(f"**Successfully Send Message To** `{sent}` **Group, Failed to Send Message To** `{failed}` **Group**")
            await asyncio.sleep(0.7)
        await message.reply_text(f"**Send Message To** `{sent}` **Group, Failed to Send Message To** `{failed}` **Group**")




@Client.on_message(filters.command(["chatbroadcast", "broadcast", "br", "gcast"]) & filters.user(SUDO_USERS))
async def chat_broadcast(c: Client, m: Message):
    if m.reply_to_message:
        msg = m.reply_to_message.text.markdown
    else:
        await m.reply_text("Usage: /gcast for bot\n /agcast broadcast By assistant\n\n**Reply to any text message for gcast**")
        return

    exmsg = await m.reply_text("Started broadcasting!")
    err_str, done_broadcast = "", 0

    async for dialog in c.iter_dialogs():
          try:
                await c.send_message(dialog.chat.id, msg, disable_web_page_preview=True)
                done_broadcast += 1
                await asyncio.sleep(0.1)
          except Exception as e:
            await m.reply_text(f"[Broadcast] {dialog.chat.id} {e}")




@Client.on_message(filters.command(["achatbroadcast", "abroadcast", "abr", "agcast"]) & filters.user(SUDO_USERS))
async def chat_broadcast(c: Test, m: Message):
    if m.reply_to_message:
        msg = m.reply_to_message.text.markdown
    else:
        await m.reply_text("Usage: /gcast for bot\n /agcast broadcast By assistant\n\n**Reply to any text message for gcast**")
        return

    exmsg = await m.reply_text("Started broadcasting!")
    err_str, done_broadcast = "", 0

    async for dialog in c.iter_dialogs():
          try:
                await c.send_message(dialog.chat.id, msg, disable_web_page_preview=True)
                done_broadcast += 1
                await asyncio.sleep(0.1)
          except Exception as e:
            await m.reply_text(f"[Broadcast] {dialog.chat.id} {e}")



