#!/usr/bin/env python3
# This is bot coded by Abhijith N T and used for educational purposes only
# https://github.com/AbhijithNT
# Copyright ABHIJITH N T
# Thank you https://github.com/pyrogram/pyrogram

from bot.filetocloud import CloudBot, filters
from bot import Msg

@CloudBot.on_message(filters.command("start"))
async def start_message(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"سلام این ربات میتونه فایلای شمارو توی چهار سایت آپلود کنه و دایرکت لینک بده 👌",
        reply_to_message_id=message.message_id,
        parse_mode="html"
    )
@CloudBot.on_message(filters.command(["help", "h"]))
async def help_message(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"سلام این ربات میتونه فایلای شمارو توی چهار سایت آپلود کنه و دایرکت لینک بده 👌",
        reply_to_message_id=message.message_id,
        parse_mode="html"
    )
