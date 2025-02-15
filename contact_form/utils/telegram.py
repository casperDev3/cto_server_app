from aiogram import Bot
from aiogram.enums import ParseMode
from asgiref.sync import async_to_sync
import os

bot_token = os.environ.get('TELEGRAM_CONTACT_BOT_TOKEN')
chat_id = os.environ.get('TELEGRAM_CONTACT_CHAT_ID')

@async_to_sync
async def send_message_async(message):
    if not bot_token or not chat_id:
        raise Exception('Bot Token or Chat ID not configured')
    bot = Bot(token=bot_token)
    try:
        await bot.send_message(chat_id=chat_id, text=message, parse_mode=ParseMode.HTML)
    except Exception as e:
        raise e
    finally:
        await bot.session.close()
