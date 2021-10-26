import logging
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.menuKeyboard import menu
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    logging.info(message)
    await message.answer(f"Assalomu aleykum, <i>{message.from_user.full_name}!</i>\n <u>mohirdev.uz</u> platformasi botiga xush kelibsiz!\n"
                         f"Kurslar ro\'yxatini ko\'rishni istasangiz <b>/menu</b> ni bosing.", reply_markup=menu)

