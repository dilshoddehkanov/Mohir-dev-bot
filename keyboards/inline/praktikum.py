from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

Praktikum_1 = InlineKeyboardMarkup(row_width=2)

Praktikum_1_link = {
    'Data Science' : 'https://ai.mohirdev.uz/?_ga=2.34796129.1751424589.1635194870-486149279.1634758498',
    'Digital Marketing' : 'https://digital.mohirdev.uz/?_ga=2.91263257.2097863619.1635195402-486149279.1634758498',
    'Front End Development' : 'https://frontend.mohirdev.uz/?_ga=2.204796304.1030532849.1635195432-486149279.1634758498',
    'Python' : 'https://python.mohirdev.uz/?_ga=2.209038802.1560378161.1635195474-486149279.1634758498',
    'MERN' : 'https://mern.mohirdev.uz/?_ga=2.205746769.339373987.1635195647-486149279.1634758498',
}

for key, value in Praktikum_1_link.items():
    PraktikumButton = InlineKeyboardButton(text=key, url=value)
    Praktikum_1.insert((PraktikumButton))

Praktikum_2 = InlineKeyboardMarkup(row_width=2)

Praktikum_2_link = {
    'English For IT' : 'https://english.mohirdev.uz/?_ga=2.13465527.1616318449.1635195665-486149279.1634758498',
    'Go' : 'https://go.mohirdev.uz/?_ga=2.263979852.114726582.1635195692-486149279.1634758498',
    'Project Management' : 'https://pm.mohirdev.uz/?_ga=2.235200769.1022275040.1635195709-486149279.1634758498',
    'Android Development': 'https://android.mohirdev.uz/?_ga=2.28325628.1592889544.1635195782-486149279.1634758498',
    'IOS Development': 'https://ios.mohirdev.uz/?_ga=2.44426980.1368116934.1635195830-486149279.1634758498',
    'Java Developer': 'https://java.mohirdev.uz/?_ga=2.58879275.78073454.1635195851-486149279.1634758498',
}

for key, value in Praktikum_2_link.items():
    PraktikumButton = InlineKeyboardButton(text=key, url=value)
    Praktikum_2.insert((PraktikumButton))
