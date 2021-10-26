from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_course = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='.NET'),
            KeyboardButton(text='Back-end'),
            KeyboardButton(text='Data Science'),
        ],
        [
            KeyboardButton(text='DevOps'),
            KeyboardButton(text='Foundation'),
            KeyboardButton(text='JavaScript'),
        ],
        [
            KeyboardButton(text='Mobile dasturlash'),
            KeyboardButton(text='Python'),
            KeyboardButton(text='React.js'),
        ],
        [
            KeyboardButton(text='HTML, CSS, Bootstrap'),
            KeyboardButton(text='⬅️Orqaga'),
        ],
    ],
    resize_keyboard=True
)

menu_praktika = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='1️⃣ Praktikum'),
            KeyboardButton(text='2️⃣ Praktikum'),
        ],
        [
            KeyboardButton(text='⬅️Orqaga')
        ],
    ],
    resize_keyboard=True
)