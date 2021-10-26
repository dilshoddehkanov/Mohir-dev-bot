from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

NETKeyboard = InlineKeyboardMarkup(row_width=1)

net = InlineKeyboardButton(text='ASP .Net Core MVC-batafsil', url='https://mohirdev.uz/courses/asp-net-core-mvc-batafsil/')
NETKeyboard.insert(net)

BackendKeyboard = InlineKeyboardMarkup(row_width=2)

BackendKeyboard_link = {
    'Proffessional Node.JS. Noldan e\'lonlar saytini yaratamiz' : 'https://mohirdev.uz/courses/professional-node-js-noldan-elonlar-saytini-yaratamiz-2',
    'Django Rest Framework darslari' : 'https://mohirdev.uz/courses/django-rest-framework-darslari/',
    'Php dasturlash tili asoslari' : 'https://mohirdev.uz/courses/php-dasturlash-tili-asoslari/',
    'Node.JSda amaliyot. Blog loyihasi' : 'https://mohirdev.uz/courses/nodejsda-amaliyot-blog-loyihasi/',
    'Docker haqida batafsil' : 'https://mohirdev.uz/courses/docker-haqida-batafsil/',
    'TensorFlow.js ga kirish' : 'https://mohirdev.uz/courses/tensorflow-js-ga-kirish/',
    'GO dasturlash tili' : 'https://mohirdev.uz/courses/go-dasturlash-tili/',
    'Dajngo 3 - Pythonda Full stack Web Dasturlash' : 'https://mohirdev.uz/courses/django/',

}
for key, value in BackendKeyboard_link.items():
    BackendButton = InlineKeyboardButton(text=key, url=value)
    BackendKeyboard.insert((BackendButton))

DataScienceKeyboard = InlineKeyboardMarkup(row_width=1)

tensor = InlineKeyboardButton(text='TensorFlow.js ga kirish', url='https://mohirdev.uz/courses/tensorflow-js-ga-kirish/')
DataScienceKeyboard.insert(tensor)

DevopsKeyboard = InlineKeyboardMarkup(row_width=1)

git = InlineKeyboardButton(text='Git versiya boshqaruv tizimi', url='https://mohirdev.uz/courses/git-versiya-boshqaruv-tizimi/')
DevopsKeyboard.insert(git)

docker = InlineKeyboardButton(text='Docker haqida batafsil', url='https://mohirdev.uz/courses/docker-haqida-batafsil/')
DevopsKeyboard.insert(docker)

FoundationKeyboard = InlineKeyboardMarkup(row_width=1)

Foundation_link = {
    'Algoritmlar: Leetcodeda masala yechish' : 'https://mohirdev.uz/courses/algoritmlar-leetcode-da-masala-yechish/',
    'C++ dasturlash asoslari' : 'https://mohirdev.uz/courses/c-dasturlash-asoslari/',
    'Dasturlash asoslari. Python' : 'https://mohirdev.uz/courses/python/',
    'Ma\'lumotlar tuzilmasi va algoritmlar' : 'https://mohirdev.uz/courses/algoritmlar/',
}

for key, value in Foundation_link.items():
    FoundationButton = InlineKeyboardButton(text=key, url=value)
    FoundationKeyboard.insert((FoundationButton))


JSKeyboard = InlineKeyboardMarkup(row_width=2)

JSKeyboard_link = {
    'Blue ReactJS (O\'zbek tilidagi react kursi)' : 'https://mohirdev.uz/courses/blue-react-js-ozbek-tilidagi-react-kursi/',
    'Node.JSda amaliyot. Blog loyihasi' : 'https://mohirdev.uz/courses/nodejsda-amaliyot-blog-loyihasi/',
    'TypeScript asoslari' : 'https://mohirdev.uz/courses/typescript-asoslari/',
    'SOLID Tamomyillari' : 'https://mohirdev.uz/courses/solid-tamoyillari/',
    'JavaScript to\'liq kurs - "From 0 to Hero"' : 'https://mohirdev.uz/courses/javascript-toliq-kurs-from-0-to-hero/',
    'Full-Stack ReactJS. Real projects' : 'https://mohirdev.uz/courses/full-stack-reactjs-real-proyektlar/',
    'Full-Stack JavaScript to\'liq kurs va praktikalar' : 'https://mohirdev.uz/courses/full-stack-javascript-toliq-kurs-va-praktikalar/'
}

for key, value in JSKeyboard_link.items():
    JSButton = InlineKeyboardButton(text=key, url=value)
    JSKeyboard.insert((JSButton))

MobileKeyboard = InlineKeyboardMarkup(row_width=1)

MobileKeyboard_link = {
    'Flutter - Android & iOS mobil dasturlash (Boshlovchilar uchun)' : 'https://mohirdev.uz/courses/flutter-android-ios-mobil-dasturlash-boshlovchilar-uchun/',
    'Xcode - Oddiy test ilovasini ishlab chiqish' : 'https://mohirdev.uz/courses/xcode-oddiy-test-ilovasini-ishlab-chiqish/',
    'Android studio - Retrofit bilan ishlash' : 'https://mohirdev.uz/courses/android-studio-retrofit-bilan-ishlash/',
    'StartDroid - Android ilovalar tuzish' : 'https://mohirdev.uz/courses/startdroid-android-ilovalar-tuzish/',
}

for key, value in MobileKeyboard_link.items():
    MobileButton = InlineKeyboardButton(text=key, url=value)
    MobileKeyboard.insert((MobileButton))

PythonKeyboard = InlineKeyboardMarkup(row_width=1)

PythonKeyboard_link = {
    'Mukammal Telegram Bot' : 'https://mohirdev.uz/courses/telegram/',
    'Dasturlash asoslari. Python' : 'https://mohirdev.uz/courses/python/',
    'Dajngo 3 - Pythonda Full stack Web Dasturlash' : 'https://mohirdev.uz/courses/django/',
    'Ma\'lumotlar tuzilmasi va algoritmlar' : 'https://mohirdev.uz/courses/algoritmlar/',
}

for key, value in PythonKeyboard_link.items():
    PythonButton = InlineKeyboardButton(text=key, url=value)
    PythonKeyboard.insert((PythonButton))

ReactKeyboard = InlineKeyboardMarkup(row_width=1)

ReactKeyboard_link = {
    'Blue ReactJS (O\'zbek tilidagi react kursi)' : 'https://mohirdev.uz/courses/blue-react-js-ozbek-tilidagi-react-kursi/',
    'ReactJS To\'liq kurs - "From 0 to Hero". 10 ta real loyiha' : 'https://mohirdev.uz/courses/react-js-toliq-kurs-from-0-to-hero-10ta-real-loyiha/',
    'React asoslari 2021' : 'https://mohirdev.uz/courses/react-asoslari-2021/',
}

for key, value in ReactKeyboard_link.items():
    ReactButton = InlineKeyboardButton(text=key, url=value)
    ReactKeyboard.insert((ReactButton))

FrontKeyboard = InlineKeyboardMarkup(row_width=1)

FrontKeyboard_link = {
    'Bootstrap 5 bo\'yicha mukammal kurs (2021)' : 'https://mohirdev.uz/courses/bootstrap-5-boyicha-mukammal-kurs-2021/',
    'HTMLda dasturlash' : 'https://mohirdev.uz/courses/htmlda-dasturlash/',
    '45 minutda HTML5' : 'https://mohirdev.uz/courses/45-minutda-html5/',
    'CSS bo\'yicha mukammal kurs (2021)' : 'https://mohirdev.uz/courses/css-2021/',
}

for key, value in FrontKeyboard_link.items():
    FrontButton = InlineKeyboardButton(text=key, url=value)
    FrontKeyboard.insert((FrontButton))