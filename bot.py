# noinspection PyInterpreter
from telegram.ext import ApplicationBuilder, MessageHandler, filters, CallbackQueryHandler, CommandHandler # Импортирование библиотек

from gpt import * # Импортирование библиотек
from util import * # Импортирование библиотек

# тут будем писать наш код :)
# Часто встречаемые аргументы:
# update - содержит информацию о событии (например, нажатие кнопки)
# context - предоставляет контекст выполнения (например, доступ к данным пользователя).

async def start(update, context): # В этой строке мы инициализируем нашу функцию для кнопки старт
    text = load_message("main") # переменная для заготовленного текста; он находится в resources\messages\main.txt <------|
    await send_photo(update, context, "main") # ответ от бота - отправка фотографии resources\images\main.img       |
    await send_text(update, context, text) # ответ от бота - отправка текста с помощью переменной "text" из 13 строки ____|

# Что за async и await?
# async нужен для того, чтобы функцию сделать асинхронной (быстрой)
# await может использоваться внутри функции с использованием async, используется для асинхронизации кода
# ТЫ ВСЁ СМОЖЕШЬ :)


async def hello(update, context): # В этой строке мы инициализируем нашу функцию для кнопки реагирования на сообщения
    await send_text(update, context,"*Привет*") # ответ от бота - отправка текста
    await send_text(update, context,"_Как дела?_") # ответ от бота - отправка текста
    await send_text(update, context,"Вы написали " + update.message.text) # ответ от бота - отправка текста |
    # "Вы написали " + update.message.text -- думаю тут понятно, что происходит: "Вы написали " - просто текст |
    # + update.message.text - берется само сообщение от пользователя
    await send_photo(update, context, "avatar_main") # ответ от бота - отправка фотографии
    await send_text_buttons(update, context, "Запустить процесс?", {
        "start": "Запустить",
        "stop": "Остановить"
    }) # ответ от бота в виде красивых кнопочек (часто их называют "инлайн" кнопками)

async def hello_button(update, context): # А эта функция - обработчик событий.
    #Проще говоря, он реагирует на нажатие той или иной красивой как ТЫ, кнопочки
    query = update.callback_query.data # query хранит данные, связанные с нажатой кнопкой, которые передаются в callback_query.data.
    if query == "start": # Условие ЕСЛИ нажатие было на кнопочку "start" , то выполняется действие на след строке
        await send_text(update, context, "Процесс запущен") # ответ от бота - отправка текста
    else: #Условие ЕЩЁ нажатие было не на кнопочку "start" , то выполняется действие на след строке
        await send_text(update, context, "Процесс остановлен") # ответ от бота - отправка текста


# Don't say that You're stupid or smthng like that, EVERYBODY HAS RIGHTS FOR MISTAKES


app = ApplicationBuilder().token("8007104072:AAH-y89AH4J7UpyMsuUwe5fr7NAR-jDwq2Y").build() # Связывание всего этого кода с ботом. Тут обязательно не забудь вставить СВОЙ токен
app.add_handler(CommandHandler("start", start)) # добавляет обработчик команд для команды /start.
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, hello)) # Здесь добавляется обработчик для текстовых сообщений, которые не являются командами.
app.add_handler(CallbackQueryHandler(hello_button)) #добавляет обработчик для колбек-запросов, которые возникают при нажатии на кнопки в интерфейсе Telegram.
app.run_polling() # Этот метод запускает бота в режиме "polling", что означает, что бот будет постоянно проверять наличие новых обновлений (сообщений, команд и т.д.) от Telegram.
