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
               text="""𝐇𝐀𝐈 𝐈 𝐀𝐌 𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐏𝐇 𝐔𝐏𝐋𝐎𝐀𝐃𝐄𝐑 𝐁𝐎𝐓. 
               𝐈 𝐂𝐀𝐍 𝐔𝐏𝐋𝐎𝐀𝐃 𝐏𝐇𝐎𝐓𝐎𝐒 𝐔𝐍𝐃𝐄𝐑 5𝐌𝐁 𝐎𝐍 telegra.ph.""",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                    InlineKeyboardButton(
                                            "🎧𝐒𝐔𝐏𝐏𝐎𝐑𝐓 𝐆𝐑𝐎𝐔𝐏🎧", url="https://t.me/NAZRIYASUPPORT")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@tgraph.on_message(filters.photo)
async def tgraphphoto(client, message):
    msg = await message.reply_text("𝐖𝐀𝐈𝐓 𝐀 𝐌𝐎𝐌𝐄𝐍𝐓 😴 𝐔𝐏𝐋𝐎𝐀𝐃𝐈𝐍𝐆 𝐓𝐎 𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐏𝐇.........")
    download_location = await client.download_media(
        message=message, file_name='root/tg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("𝐒𝐈𝐙𝐄 𝐎𝐅 𝐓𝐇𝐄 𝐏𝐇𝐎𝐓𝐎 𝐒𝐇𝐎𝐔𝐋𝐃 𝐁𝐄 𝐋𝐄𝐒𝐒 𝐓𝐇𝐀𝐍 5 𝐌𝐁.") 
    else:
        await msg.edit_text(f'**𝐔𝐏𝐋𝐎𝐀𝐃𝐄𝐃 𝐓𝐎 𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐏𝐇!\n\n👉 https://telegra.ph{response[0]}\n\n𝐁𝐘 telegra.ph**',
            disable_web_page_preview=True,
        )        
