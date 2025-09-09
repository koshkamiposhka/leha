import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from db import SessionLocal, CustomUser

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    if len(context.args) != 1:
        await update.message.reply_text("Используйте: /start <номер телефона>")
        return

    phone = context.args[0]

    session = SessionLocal()
    user = session.query(CustomUser).filter_by(phone=phone).first()
    if not user:
        await update.message.reply_text("Пользователь с таким номером не найден.")
        session.close()
        return

    other = session.query(CustomUser).filter_by(telegram_id=str(chat_id)).first()
    if other:
        other.telegram_id = None
        session.add(other)

    user.telegram_id = str(chat_id)
    session.add(user)
    session.commit()
    session.close()

    await update.message.reply_text("Вы успешно зарегистрированы в системе!")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Бот запущен...")
    app.run_polling()
