from telebot import types


def get_keyboard_cat(categories, btn_link):
    row = 3
    keyboard = types.InlineKeyboardMarkup(row_width = row)
    btns = []
    for category in categories:
        if category[4] == 1:
            btn_link = btn_link + str(category[0])
            btns.append(types.InlineKeyboardButton(text = category[1], callback_data = btn_link))

    return(keyboard.add(*btns))

def get_keyboard_prod(products, btn_link):
    row = 2
    keyboard = types.InlineKeyboardMarkup(row_width = row)
    btns = []
    for product in products:
        btn_link = btn_link + str(product[0])
        btns.append(types.InlineKeyboardButton(text = product[1], callback_data = btn_link))

    return(keyboard.add(*btns))

def get_keyboard_meats_quantity(btn_link):
    row = 3
    keyboard = types.InlineKeyboardMarkup(row_width = row)
    btns = []
    for i in range(1, 11):
        btns.append(types.InlineKeyboardButton(text = str(i), callback_data = btn_link + str(i)))

    return (keyboard.add(*btns))


def get_keyboard_verify_orders(btn_link):
    row = 2
    keyboard = types.InlineKeyboardMarkup(row_width = row)

    button_yes = types.InlineKeyboardButton(text = "Да", callback_data = btn_link + 'yes')
    button_no = types.InlineKeyboardButton(text = "Нет", callback_data = btn_link + 'no')
    return(keyboard.add(button_yes, button_no))
