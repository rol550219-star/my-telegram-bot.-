import os
from aiogram import Bot, Dispatcher, types
import asyncio
import logging

# Токен береться безпечно з налаштувань сервера (Render/Railway)
TOKEN = os.environ.get("TOKEN")

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
                    await message.delete()
                    await message.answer(f"@{message.from_user.username}, не матерись!")
                except Exception as e:
                    print(f"Помилка видалення: {e}")
                break

async def main():
    if not TOKEN:
        print("ПОМИЛКА: Токен не знайдено! Перевір налаштування Environment Variables.")
        return
        
    bot = Bot(token=TOKEN)
    print("Бот запущений і надійно тримає зв'язок!")
    await dp.start_polling(bot, drop_pending_updates=True, polling_timeout=60)

if __name__ == "__main__":
    asyncio.run(main())
  
