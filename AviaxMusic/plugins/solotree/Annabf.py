import asyncio
from pyrogram import filters
from pyrogram.enums import ChatMembersFilter
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random
from AviaxMusic import app
from AviaxMusic.utils.database import get_served_chats

# Updated quotes format
quotes = [
    """<b>🎯 𝖸𝗈𝗎𝗋 𝖶𝗂𝗇𝗇𝗂𝗇𝗀 𝖩𝗈𝗎𝗋𝗇𝖾𝗒 𝖲𝗍𝖺𝗋𝗍𝗌 𝖧𝖾𝗋𝖾!</b> \n\n<u>💎 𝖳𝗈𝗉 𝖦𝖺𝗆𝖾𝗌 𝖶𝖾 𝖮𝖿𝖿𝖾𝗋:</u>\n\n<b>[🎟 𝖠𝗇𝗇𝖺 𝖫𝗈𝗍𝗍𝖾𝗋𝗒 𝖦𝖺𝗆𝖾](http://t.me/SpikyMusicBot/Annalottery)</b> – 𝖯𝗅𝖺𝗒 𝗒𝗈𝗎𝗋 𝗅𝗎𝖼𝗄 𝖺𝗇𝖽 𝗐𝗂𝗇 𝗅𝗂𝗄𝖾-𝖼𝗁𝖺𝗇𝗀𝗂𝗇𝗀 𝗉𝗋𝗂𝗓𝖾𝗌!\n\n<b>🌈 𝖢𝗈𝗅𝗈𝗎𝗋 𝖳𝗋𝖺𝖽𝗂𝗇𝗀</b> – 𝖯𝗋𝖾𝖽𝗂𝖼𝗍 𝖺𝗇𝖽 𝗉𝗋𝗈𝖿𝗂𝗍 𝗐𝗂𝗍𝗁 𝖾𝖺𝗌𝖾!\n\n<b>🛫 𝖠𝗏𝗂𝖺𝗉𝗈𝗋 𝖦𝖺𝗆𝖾𝗌</b> – 𝖲𝖼𝗋𝖺𝗍𝖼𝗁, 𝗋𝖾𝗏𝖾𝖺𝗅, 𝖺𝗇𝖽 𝗐𝗂𝗇 𝗂𝗇𝗌𝗍𝖺𝗇𝗍𝗅𝗒!\n\n<b>🎰 𝖢𝖺𝗌𝗂𝗇𝗈 𝖦𝖺𝗆𝖾𝗌</b> – 𝖲𝗉𝗂𝗇 𝖺𝗇𝖽 𝖿𝖾𝖾𝗅 𝗍𝗁𝖾 𝗍𝗁𝗋𝗂𝗅𝗅 𝗈𝖿 𝖵𝖾𝗀𝖺𝗌 𝖺𝗍 𝗁𝗈𝗆𝖾!\n\n<b>⚡𝖠𝗅𝗅 𝖫𝗂𝗏𝖾 𝖲𝗉𝗈𝗋𝗍𝗌 𝖡𝖾𝗍𝗍𝗂𝗇𝗀</b> – 𝖡𝖾𝗍 𝗂𝗇 𝗋𝖾𝖺𝗅-𝗍𝗂𝗆𝖾 𝖺𝗇𝖽 𝖾𝗑𝗉𝗂𝗋𝗂𝖾𝗇𝖼𝖾 𝗍𝗁𝖾 𝖺𝗅𝗂𝗏𝖾𝗇𝗍𝗁𝗒!\n\n╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼\n\n<u><b>💰 𝖯𝗅𝖺𝗒 𝖭𝗈𝗐 & 𝖦𝖾𝗍 𝖱𝖾𝗐𝖺𝗋𝖽𝗌!</b></u>\n\n💸 𝖤𝖺𝗌𝗒 𝗍𝗈 𝗉𝗅𝖺𝗒 𝖺𝗇𝖽 𝗐𝗂𝗇.\n\n💲 𝖨𝗇𝗌𝗍𝖺𝗇𝗍 𝗐𝗂𝗍𝗁𝖽𝗋𝖺𝗐𝖺𝗅𝗌 𝖺𝗍 𝗒𝗈𝗎𝗋 𝖼𝗈𝗇𝗏𝖾𝗇𝗂𝖾𝗇𝖼𝖾.\n\n🔒 𝖲𝖺𝖿𝖾 𝖺𝗇𝖽 𝗌𝖾𝖼𝗎𝗋𝖾 𝗉𝗅𝖺𝗍𝖿𝗈𝗋𝗆""",
    # Add more quotes if needed...
]

IS_BROADCASTING = False

async def auto_broadcast():
    global IS_BROADCASTING
    IS_BROADCASTING = True

    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton("💸 𝖯𝗅𝖺𝗒 𝖭𝗈𝗐 🎮", url="http://t.me/SpikyMusicBot/Annalottery")]]
    )

    while True:
        sent = 0
        schats = await get_served_chats()

        for chat in schats:
            # Select a random quote from the quotes list
            message_text = random.choice(quotes)

            try:
                await app.send_message(chat["chat_id"], text=message_text, reply_markup=keyboard)
                sent += 1
                await asyncio.sleep(0.2)
            except FloodWait as fw:
                flood_time = int(fw.value)
                if flood_time > 200:
                    continue
                await asyncio.sleep(flood_time)
            except Exception:
                continue

        # Wait for 6 hours before the next broadcast
        await asyncio.sleep(21600)

# Start the auto-broadcast function
app.add_handler(asyncio.create_task(auto_broadcast()))