import craft_meats_db

import buttons

from craft_meats_bot.contactapp.contact import contact_us
from craft_meats_bot.orderapp.order import order_app
from craft_meats_bot.my_orders.my_orders import get_my_orders
from craft_meats_bot.storageapp.storage import storege_app
from craft_meats_bot.mainapp import keyboards
from craft_meats_bot.my_data import bot


# bot.remove_webhook()


# ---------------------------------------------------------------------------
# Приветствие пользователя

@bot.message_handler(commands = ['start', 'help'])
def send_welcome(message):
    user_list = (int(message.from_user.id), message.from_user.first_name, message.from_user.username)

    craft_meats_db.users_insert_new(user_list)
    bot.reply_to(message, f"{message.from_user.first_name}, привет!! Я Мясной_Бот, я помогу тебе заказать вкусняшку!")

    bot.send_message(message.from_user.id, text = "Выбирай нужное меню!",
                     reply_markup = keyboards.get_main_menu(message.from_user.id))


# ---------------------------------------------------------------------------
# Информация

TXT_ABOUT_US = "Мы занимаемся производством вкусного сыровяленнго мяса и не только! " \
               "Так как процесс вяления мяса не быстрый, от 4-х месяцев, " \
               "то для того чтобы все желающие получили долгожданное мясо был создан Я. " \
               "Я создаю электронную очередь желающих, собираю все контактные данные и " \
               "буду опевещать Вас о старте производства и готовности вкусняшек. Я еще маленький и только учусь, " \
               "поэтому первое время мой создатель будет меня контролировать :)\n\n " \
               "Так же время от времени мы делаем другие виды мяса: сырокопченые, копчено-вареные, колбасы \n\n " \
               "Написать создателю @Andrei_shcherbina"


@bot.message_handler(commands = ['info'])
def print_info_about_us(message):
    bot.reply_to(message, TXT_ABOUT_US)
    bot.send_message(message.from_user.id, text = "Выбирай нужное меню!",
                     reply_markup = keyboards.get_main_menu(message.from_user.id))


@bot.message_handler(commands = ['menu', 'меню', 'Меню', 'Menu'])
def print_menu(message):
    text = "Главное меню:"
    bot.send_message(message.chat.id, text = text, reply_markup = keyboards.get_main_menu(message.from_user.id))


# TODO добавить условия перехода в order и storage
@bot.callback_query_handler(func = lambda call: True)
def call_back_main(call):
    if buttons.MY_ORDERS in call.data:
        get_my_orders(call)
    elif buttons.ORDER in call.data:
        order_app(call)
    elif buttons.GET_STORAGE_INFO in call.data:
        storege_app(call)
    elif buttons.INFO_ABOUT_US in call.data:
        bot.send_message(call.message.chat.id, text = TXT_ABOUT_US)
    elif buttons.CONTACT in call.data:
        contact_us(call)



bot.infinity_polling()
