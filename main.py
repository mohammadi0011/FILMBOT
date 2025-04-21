import os
import logging
from aiogram import Bot, Dispatcher, types, executor

# Retrieve the bot token from environment variable
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN environment variable is not set")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("🎬 سلام! به ربات فیلم‌یاب خوش آمدید.\nلطفا نام فیلم یا سریال را ارسال کنید.")

@dp.message_handler()
async def handle_message(message: types.Message):
    text = message.text.strip()
    # Placeholder for actual search logic
    # For now, respond with a stub message and buttons
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        types.InlineKeyboardButton("زبان اصلی", callback_data="lang_original"),
        types.InlineKeyboardButton("دوبله فارسی", callback_data="lang_dubbed"),
        types.InlineKeyboardButton("زیرنویس چسبیده", callback_data="sub_embedded"),
    )
    keyboard.add(
        types.InlineKeyboardButton("VLC", callback_data="player_vlc"),
        types.InlineKeyboardButton("MX", callback_data="player_mx")
    )
    await message.reply(f"🔍 در حال جستجوی: {text}\n(این نسخه تست است.)", reply_markup=keyboard)

@dp.callback_query_handler(lambda c: True)
async def process_callback(callback_query: types.CallbackQuery):
    data = callback_query.data
    await callback_query.answer(f"شما گزینه {data} را انتخاب کردید.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
