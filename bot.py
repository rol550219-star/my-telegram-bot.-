from aiogram import Bot, Dispatcher, types
from aiogram.types import ChatPermissions
import asyncio
import logging
from datetime import datetime, timedelta

# Обов'язково встав сюди свій токен
TOKEN = "8691182355:AAGdU8A9PBW0DFIThCPWZGJKqWysq_kgRMk"

# Налаштування логування
logging.basicConfig(level=logging.INFO)

bad_words = [
    "блядь", "блять", "сука", "хуй", "нахуй", "пізда", "пизда", "ебать", "йоб", "fuck", "shit", "bitch",
    "я твою мать ебал", "я твою мам ебав"
]

dp = Dispatcher()

@dp.message()
async def check_message(message: types.Message):
    if message.text:
        text = message.text.lower()
        
        for word in bad_words:
            if word in text:
                try:
                    # 1. Видаляємо повідомлення
                    await message.delete()
                    
                    # 2. Розраховуємо час: зараз + 1 година
                    until_date = datetime.now() + timedelta(hours=1)
                    
                    # 3. Банимо користувача (забороняємо надсилати повідомлення)
                    await message.bot.restrict_chat_member(
                        chat_id=message.chat.id,
                        user_id=message.from_user.id,
                        until_date=until_date,
                        permissions=ChatPermissions(can_send_messages=False)
                    )
                    
                    await message.answer(f"@{message.from_user.username} отримав бан на 1 годину за мат!")
                    print(f"Користувач {message.from_user.username} забанений за мат.")
                except Exception as e:
                    print(f"Помилка при спробі видалити або забанити: {e}")
                break

async def main():
    bot = Bot(token=TOKEN)
    print("Бот запущений!")
    await dp.start_polling(bot, drop_pending_updates=True, polling_timeout=60)

if __name__ == "__main__":
    asyncio.run(main())
    
