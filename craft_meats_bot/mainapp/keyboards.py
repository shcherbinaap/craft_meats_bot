from telebot import types
from craft_meats_bot.mainapp import buttons
from craft_meats_bot import my_data

# ---------------------------------------------------------------------------
# Меню
def get_main_menu(user_id):
    row = 2
    keyboard = types.InlineKeyboardMarkup(row_width = row)
    btns = []
    btns.append(buttons.button_start_order)
    btns.append(buttons.button_info_about_us)
    btns.append(buttons.button_get_contact)
    btns.append(buttons.button_my_orders)  # TODO
    btns.append(buttons.button_get_storage_info)  # TODO
    if int(user_id) == my_data.MY_USER_ID:

        btns.append(buttons.button_meats_info)  # TODO
        btns.append(buttons.button_dostavka_info)  # TODO
        btns.append(buttons.button_put_storage_info)  # TODO
        btns.append(buttons.button_buying_meat)  # TODO

    keyboard.add(*btns)
    return keyboard