import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from telegraph import upload_file

tgraph = Client(
    "TELEGRAPH BOT",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

@tgraph.on_message(filters.command("start"))
async def start(client, message):
   if message.chat.type == 'private':
       await tgraph.send_message(
               chat_id=message.chat.id,
               text="""HAI I AM TELEGRAPH UPLOADER BOT. 
               I CAN UPLOAD PHOTOS UNDER 5MB ON telegra.ph.""",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                    InlineKeyboardButton(
                                            "🎧SUPPORT GROUP🎧", url="https://t.me/NAZRIYASUPPORT")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")
