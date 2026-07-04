from aiogram import Bot, Dispatcher, types
from aiogram.types import ChatPermissions
import asyncio
import logging
from datetime import datetime, timedelta

# Твій токен
TOKEN = "8691182355:AAGdU8A9PBW0DFIThCPWZGJKqWysq_kgRMk"

logging.basicConfig(level=logging.INFO)

# Повний оновлений словник
bad_words = [
    "блядь", "блять", "сука", "хуй", "нахуй", "пізда", "пизда", "ебать", "йоб", "fuck", "shit", "bitch",
    "я твою мать ебал", "я твою маму ебал",
    # Варіанти "це пиздець":
    "це пиздець", "це пипець", "це піздець", "это пиздец", "это пипец", 
    "eto pizdec", "tse pizdec", "this is shit", "this is fucked",
    # Варіанти "еблан":
    "еблан", "eblan", "eblanchik", "ебланище",
    # Трах та похідні:
    "трах", "трахал", "трахати", "трахає", "трахаюсь", "trah", "trahal",
    # Варіанти з "сіськами":
    "сіськи", "сиськи", "сиська", "сіська", "сися", "сіся", "tits", "boobs"
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
                    
                    # 2. Бан на 1 годину
                    until_date = datetime.now() + timedelta(hours=1)
                    await message.bot.restrict_chat_member(
                        chat_id=message.chat.id,
                        user_id=message.from_user.id,
                        until_date=until_date,
                        permissions=ChatPermissions(can_send_messages=False)
                    )
                    
                    # 3. Попередження в чат
                    await message.answer(f"@{message.from_user.username}, бан на 1 годину за порушення правил!")
                except Exception as e:
                    print(f"Помилка: {e}")
                break

async def main():
    bot = Bot(token=TOKEN)
    print("Бот працює на повну потужність!")
    await dp.start_polling(bot, drop_pending_updates=True, polling_timeout=60)

if __name__ == "__main__":
    asyncio.run(main())
                
