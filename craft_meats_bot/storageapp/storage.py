from craft_meats_bot.storageapp import storage_db
from craft_meats_bot.my_data import bot
from craft_meats_bot.mainapp.buttons import APP, CATEGORY, GET_STORAGE_INFO, PRODUCT, QUANTITY, STORAGE, BUTTON
import datetime

from craft_meats_bot.storageapp import storage_keyboards
from craft_meats_bot.orderapp.orders_db import order_insert_new


def get_app(call):
    return call.data.split("/")[0].split("=")[1]


def get_cat_id(call):
    return int(call.data.split("/")[1].split("=")[1])


def get_prod_id(call):
    return int(call.data.split("/")[2].split("=")[1])


def get_storage_id(call):
    return int(call.data.split("/")[3].split("=")[1])


def storage_categories(call):
    categories = storage_db.get_storage_categories()
    btn_link = APP + get_app(call) + '/' + CATEGORY
    text = "Выберите категорию продукта:"
    keyboard = storage_keyboards.get_keyboard_storage_category(categories, btn_link)
    bot.send_message(call.message.chat.id, text = text, reply_markup = keyboard)


def storage_products(call):
    text = "Категория продукта: " + storage_db.get_cat_name(get_cat_id(call))
    text = text + "\nУточните наименование продукта!"

    products = storage_db.get_storage_products(call)
    btn_link = APP + get_app(call) + '/' + CATEGORY + str(get_cat_id(call)) + '/' + PRODUCT
    keyboard = storage_keyboards.get_keyboard_storage_product(products, btn_link)

    bot.send_message(call.message.chat.id, text = text, reply_markup = keyboard)


def storage_meats_quantity(call):
    stor_info = storage_db.get_storage_meats_quantity(call)

    if len(stor_info) > 0:
        text = "Категория продукта: " + storage_db.get_cat_name(get_cat_id(call))
        text = text + "\nНаименование продукта: " + storage_db.get_prod_name(get_prod_id(call))
        text = text + "\nВыберите упаковку:"
        btn_link = APP + get_app(call) + '/' + CATEGORY + str(get_cat_id(call)) + '/' + PRODUCT + str(
            get_prod_id(call)) + '/' + STORAGE
        keyboard = storage_keyboards.get_keyboard_meats_quantity(stor_info, btn_link)
        bot.send_message(call.message.chat.id, text = text, reply_markup = keyboard)
    else:
        text = "Больше нет ("
        bot.send_message(call.message.chat.id, text = text)


def storage_confirm_orders(call):

    result = storage_db.get_storage_confirm_orders(call)

    text = f"Подтвердите заказ:\n" \
           f"Категирия продукта: {storage_db.get_cat_name(get_cat_id(call))} \n" \
           f"Наименование продукта: {storage_db.get_prod_name(get_prod_id(call))} \n" \
           f"Масса: {str(result[0])}г. \nСтоимость {str(result[1])}р"

    btn_link = APP + get_app(call) + '/' + CATEGORY + str(get_cat_id(call)) + '/' + PRODUCT + str(
        get_prod_id(call)) + '/' + STORAGE + str(get_storage_id(call)) + '/' + BUTTON
    keyboard = storage_keyboards.get_keyboard_confirm_storage_to_orders(btn_link)
    bot.send_message(call.message.chat.id, text = text, reply_markup = keyboard)


def add_orders(call):
    order_list = (
        call.message.chat.id,
        get_cat_id(call),
        get_prod_id(call),
        1,
        storage_db.get_weight(call),
        storage_db.storage_cost(call),
        1,
        1,
        datetime.date.today()
    )

    order_id = order_insert_new(order_list = order_list)

    storage_update_list = (
        get_storage_id(call),
        call.message.chat.id,
        datetime.date.today(),
        1,
        order_id
    )

    storage_db.storage_update(storage_update_list)
    text = f"Ваш заказ №{order_id} оформлен!"
    bot.send_message(call.message.chat.id, text = text)
    storage_meats_quantity(call)


def storege_app(call):
    if GET_STORAGE_INFO in call.data and CATEGORY not in call.data:
        storage_categories(call)
    elif CATEGORY in call.data and PRODUCT not in call.data:
        storage_products(call)
    elif PRODUCT in call.data and QUANTITY not in call.data and STORAGE not in call.data:
        storage_meats_quantity(call)
    elif STORAGE in call.data and BUTTON not in call.data:
        storage_confirm_orders(call)
    elif BUTTON in call.data:
        if "yes" in call.data:
            add_orders(call)
        elif "no" in call.data:
            storage_meats_quantity(call)
