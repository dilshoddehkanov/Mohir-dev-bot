from aiogram import types

from keyboards.default.coursesKeyboards import menu_praktika
from keyboards.inline.praktikum import Praktikum_1, Praktikum_2
from loader import dp

@dp.message_handler(text = '🖥Praktikum')
async def kurslar(message: types.Message):
    await message.answer('Bu bo\'limda siz videodarslar bilan birgalikda amliyotlarni'
                         'ham bajarib borasiz. Ya\'ni sizga vazifalar berib boriladi va tekshirib boriladi.'
                         ' Quyida praktikum yo\'nalishlari bilan tanishing👇👇👇', reply_markup=menu_praktika)

@dp.message_handler(text = '1️⃣ Praktikum')
async def praktikum(message: types.Message):
    await message.answer('Praktikum turkumidagi kurslarning 1-qismi👇👇👇', reply_markup=Praktikum_1)


@dp.message_handler(text = '2️⃣ Praktikum')
async def praktikum(message: types.Message):
    await message.answer('Praktikum turkumidagi kurslarning 2-qismi👇👇👇', reply_markup=Praktikum_2)