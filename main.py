from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import random
import string

bot = Bot(token="")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton(text="🔓 Simple password")
    button2 = KeyboardButton(text="🔓 Medium password")
    button3 = KeyboardButton(text="🔐 Strong password")
    kb.add(button1)
    kb.add(button2)
    kb.add(button3)

    await message.answer('👋🏻 Hello!\n🔗 Choose the password strength:', reply_markup=kb)

def generate_password(length, use_digits=False, use_specials=False):
    characters = string.ascii_lowercase + string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_specials:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

@dp.message_handler(content_types=['text'])
async def handle_message(message: types.Message):
    if message.text == "🔓 Simple password":
        password = generate_password(8)
        await message.answer(f"🔓 Your password: <code>{password}</code>", parse_mode="html")

    elif message.text == "🔓 Medium password":
        password = generate_password(12, use_digits=True)
        await message.answer(f"🔓 Your password: <code>{password}</code>", parse_mode="html")

    elif message.text == "🔐 Strong password":
        password = generate_password(16, use_digits=True, use_specials=True)
        await message.answer(f"🔐 Your password: <code>{password}</code>", parse_mode="html")

executor.start_polling(dp, skip_updates=True)