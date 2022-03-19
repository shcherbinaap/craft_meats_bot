from telebot import types
from craft_meats_bot.storageapp.storage_db import get_cat_name, get_prod_name


def get_keyboard_meats_quantity(stor_info, btn_link):
    row = 1

    btns = []
    keyboard = types.InlineKeyboardMarkup(row_width = row)

    for stor in stor_info:
        btn_link = btn_link + str(stor[0])
        text_btn = f"Масса: {str(stor[1])}г. \nСтоимость {str(stor[2])}р"
        btns.append(types.InlineKeyboardButton(text = text_btn, callback_data = btn_link))

    return keyboard.add(*btns)


def get_keyboard_confirm_storage_to_orders(btn_link):
    row = 2
    keyboard = types.InlineKeyboardMarkup(row_width = row)

    button_yes = types.InlineKeyboardButton(text = "Да", callback_data = btn_link + 'yes')
    button_no = types.InlineKeyboardButton(text = "Нет", callback_data = btn_link + 'no')
    return keyboard.add(button_yes, button_no)


def get_keyboard_storage_category(categories, btn_link):
    row = 3
    keyboard = types.InlineKeyboardMarkup(row_width = row)
    btns = []
    for category_id in categories:
        btn_link = btn_link + str(category_id[0])
        btns.append(types.InlineKeyboardButton(text = get_cat_name(category_id[0]), callback_data = btn_link))

    return keyboard.add(*btns)


def get_keyboard_storage_product(products, btn_link):
    row = 2
    keyboard = types.InlineKeyboardMarkup(row_width = row)
    btns = []
    for product in products:
        btn_link = btn_link + str(product[0])
        btns.append(types.InlineKeyboardButton(text = get_prod_name(product[0]), callback_data = btn_link))
    return keyboard.add(*btns)
