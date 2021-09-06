#импортируем нужные компаненты
import logging #модуль для логирования
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters 

import Settings#инфа с конф данными

logging.basicConfig(filename="bot.log", level=logging.INFO)#настройка логирвоания, куда записываем и лелв логирование INFO 

#настройки прокси
PROXY = {'proxy_url': Settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': Settings.PROXY_USERNAME, 'password': Settings.PROXY_PASSWORD}}

def greet_user(update, context):#апдейт - инфа которая пришла от платформы телеги, контекст - отдаем команды боту
    print("Вызван /start")
    update.message.reply_text("Здравствуй, пользователь!")

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def main():
    mybot = Updater(Settings.API_KEY, use_context=True, request_kwargs=PROXY)#токен и прокся

    dp = mybot.dispatcher #просто скоращяем название mybot.dispatcher положив в переменую dp
    dp.add_handler(CommandHandler("start", greet_user))#тут написано добавляю к диспечеру обработчик, тип обработчик команд который реогриует на команду старт и вызвают функцию грет юзер
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("bot start")#в сообщение в логах что бот стартанул
    mybot.start_polling()#стучится на сервер за обновами
    mybot.idle()#что бы бот крутился и не выкл

if __name__ == "__main__":#для импорта, что бы не сломать код
    main()