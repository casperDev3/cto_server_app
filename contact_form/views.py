import asyncio
import json
import os
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from aiogram import Bot
from aiogram.enums import ParseMode
from asgiref.sync import async_to_sync

@require_http_methods(["POST"])
def contact_us(request):
    data = json.loads(request.body)
    bot_token = os.environ.get('TELEGRAM_CONTACT_BOT_TOKEN')
    chat_id = os.environ.get('TELEGRAM_CONTACT_CHAT_ID')

    if not bot_token or not chat_id:
        return JsonResponse({
            "status": "error"
        }, status=500)



    message = (
        f"New Contact Us Form Submission:\n\n"
        f"Name: <code>{data.get('name')}</code>\n"
        f"Email: <code>{data.get('email')}</code>\n"
        f"Phone: <code>{data.get('phone')}</code>\n"
        f"Message: <code>{data.get('message')}</code>\n"
    )

    @async_to_sync
    async def send_message_async():
        bot = Bot(token=bot_token)
        try:
            await bot.send_message(chat_id=chat_id, text=message, parse_mode=ParseMode.HTML)
        finally:
            await bot.session.close()

    try:
        send_message_async()
    except:
        return JsonResponse({
            "status": "error"
        }, status=500)

    return JsonResponse({
        "status": "success"
    })