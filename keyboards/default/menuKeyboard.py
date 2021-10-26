from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='💻Kurslar'),
            KeyboardButton(text='🖥Praktikum')
        ],

    ],
    resize_keyboard=True
)