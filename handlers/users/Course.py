from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from keyboards.default.coursesKeyboards import menu_course
from keyboards.default.menuKeyboard import menu
from keyboards.inline.courses import NETKeyboard, BackendKeyboard, DataScienceKeyboard, DevopsKeyboard, \
    FoundationKeyboard, JSKeyboard, MobileKeyboard, PythonKeyboard, ReactKeyboard, FrontKeyboard
from loader import dp

@dp.message_handler(Command('menu'))
async  def show_menu(message: Message):
    await message.answer('Bizda odiiy kurslar va praktikum kurslar mavjud. Shulardan '
                         'birini tanlang.', reply_markup=menu)

@dp.message_handler(text = '💻Kurslar')
async def kurslar(message: types.Message):
    await message.answer('Kurslar yo\'nalishlari bilan tanishing👇👇👇', reply_markup=menu_course)

@dp.message_handler(text = '.NET')
async  def show_menu(message: Message):
    await message.answer('.NET yo\'nalishidahgi mavzular', reply_markup=NETKeyboard)

@dp.message_handler(text = 'Back-end')
async  def show_menu(message: Message):
    await message.answer('Bach-end yo\'nalishidahgi mavzular', reply_markup=BackendKeyboard)

@dp.message_handler(text = 'Data Science')
async  def show_menu(message: Message):
    await message.answer('Data Science yo\'nalishidahgi mavzular', reply_markup=DataScienceKeyboard)

@dp.message_handler(text = 'DevOps')
async  def show_menu(message: Message):
    await message.answer('DevOps yo\'nalishidahgi mavzular', reply_markup=DevopsKeyboard)

@dp.message_handler(text = 'Foundation')
async  def show_menu(message: Message):
    await message.answer('Foundation yo\'nalishidahgi mavzular', reply_markup=FoundationKeyboard)

@dp.message_handler(text = 'JavaScript')
async  def show_menu(message: Message):
    await message.answer('JavaScript yo\'nalishidahgi mavzular', reply_markup=JSKeyboard)

@dp.message_handler(text = 'Mobile dasturlash')
async  def show_menu(message: Message):
    await message.answer('Mobile dasturlash yo\'nalishidahgi mavzular', reply_markup=MobileKeyboard)

@dp.message_handler(text = 'Python')
async  def show_menu(message: Message):
    await message.answer('Python dasturlash yo\'nalishidahgi mavzular', reply_markup=PythonKeyboard)

@dp.message_handler(text = 'React.js')
async  def show_menu(message: Message):
    await message.answer('React.js dasturlash yo\'nalishidahgi mavzular', reply_markup=ReactKeyboard)

@dp.message_handler(text = 'HTML, CSS, Bootstrap')
async  def show_menu(message: Message):
    await message.answer('HTML, CSS, Bootstrap dasturlash yo\'nalishidahgi mavzular', reply_markup=FrontKeyboard)


@dp.message_handler(text = '⬅️Orqaga')
async  def show_menu(message: Message):
    await message.answer('Bizda odiiy kurslar va praktikum kurslar mavjud. Shulardan '
                         'birini tanlang.', reply_markup=menu)