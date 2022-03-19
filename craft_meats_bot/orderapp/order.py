from craft_meats_bot.orderapp import orders_db
from craft_meats_bot.orderapp import order_keyboards

from telebot import types
from craft_meats_bot.my_data import bot
import datetime
from craft_meats_bot.mainapp import buttons


def get_app(call):
    return (call.data.split("/")[0].split("=")[1])


def get_cat_id(call):
    return (int(call.data.split("/")[1].split("=")[1]))


def get_prod_id(call):
    return (int(call.data.split("/")[2].split("=")[1]))


def get_quant(call):
    return (int(call.data.split("/")[3].split("=")[1]))


def get_order_categories(call):
    categories = orders_db.get_categories()
    btn_link = buttons.APP + get_app(call) + '/' + buttons.CATEGORY
    keyboard = order_keyboards.get_keyboard_cat(categories, btn_link)
    text = "Выберите категорию продукта:"
    bot.send_message(call.message.chat.id, text = text, reply_markup = keyboard)


def get_order_products(call):
    products = orders_db.get_prod_in_cat(get_cat_id(call))
    btn_link = buttons.APP + get_app(call) + '/' + buttons.CATEGORY + str(get_cat_id(call)) + '/' + buttons.PRODUCT
    keyboard = order_keyboards.get_keyboard_prod(products, btn_link)
    text = "Категория продукта: " + orders_db.get_cat_name(get_cat_id(call))
    text = text + "\nУточните наименование продукта!"
    bot.send_message(call.message.chat.id, text = text, reply_markup = keyboard)


def meats_quantity(call):
    text = "Категория продукта: " + orders_db.get_cat_name(get_cat_id(call))
    text = text + "\nНаименование продукта: " + orders_db.get_prod_name(get_prod_id(call))
    text = text + "\nВыберите количесво упаковок продукта к заказу:"
    btn_link = buttons.APP + get_app(call) + '/' + buttons.CATEGORY + str(
        get_cat_id(call)) + '/' + buttons.PRODUCT + str(get_prod_id(call)) + '/' + buttons.QUANTITY
    keyboard = order_keyboards.get_keyboard_meats_quantity(btn_link)
    bot.send_message(call.message.chat.id, text = text, reply_markup = keyboard)


def verify_orders(call):
    string = f"Подтвердите заказ:\n" \
             f"Категирия продукта: {orders_db.get_cat_name(get_cat_id(call))} \n" \
             f"Наименование продукта: {orders_db.get_prod_name(get_prod_id(call))} \n" \
             f"Количество: {get_quant(call)}?"

    btn_link = buttons.APP + get_app(call) + '/' + buttons.CATEGORY + str(
        get_cat_id(call)) + '/' + buttons.PRODUCT + str(get_prod_id(call)) + '/' + buttons.QUANTITY + str(
        get_quant(call)) + '/' + buttons.BUTTON
    keyboard = order_keyboards.get_keyboard_verify_orders(btn_link)
    bot.send_message(call.message.chat.id, text = string, reply_markup = keyboard)


def push_button_yes(call):
    row = 2
    order_list = (
        call.from_user.id,
        get_cat_id(call),
        get_prod_id(call),
        get_quant(call),
        0,
        0,
        1,
        1,
        datetime.date.today()
    )

    order_id = orders_db.order_insert_new(order_list)

    text = f"Ваш заказ №{order_id} принят!\n" \
           "Как продукция будет готова Я с Вами свяжусь. \n" \
           "Хотите сделать еще заказ?"

    keyboard = types.InlineKeyboardMarkup(row_width = row)
    keyboard.add(buttons.button_start_order)

    bot.send_message(call.message.chat.id, text, reply_markup = keyboard)


def push_button_no(call):
    text = "Попробуйте сделать заказ еще раз!\n"

    bot.send_message(call.message.chat.id, text)
    get_order_categories(call)


def order_app(call):
    if buttons.ORDER in call.data and buttons.CATEGORY not in call.data:
        get_order_categories(call)
    elif buttons.CATEGORY in call.data and buttons.PRODUCT not in call.data:
        get_order_products(call)
    elif buttons.PRODUCT in call.data and buttons.QUANTITY not in call.data:
        meats_quantity(call)
    elif buttons.QUANTITY in call.data and buttons.BUTTON not in call.data:
        verify_orders(call)
    elif buttons.BUTTON in call.data:
        if "yes" in call.data:
            push_button_yes(call)
        elif "no" in call.data:
            push_button_no(call)
