import os
from telegram import Bot

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
bot = Bot(token=TELEGRAM_TOKEN)

async def send_new_order_notification(telegram_id: str, message: str = "Вам пришёл новый заказ!"):
    if telegram_id and TELEGRAM_TOKEN:
        try:
            await bot.send_message(chat_id=int(telegram_id), text=message)
        except Exception as e:
            print(f"Ошибка отправки уведомления: {e}")
