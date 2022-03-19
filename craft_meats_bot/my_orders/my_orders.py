from craft_meats_bot.my_data import bot
from craft_meats_bot.my_orders import my_orders_db


def get_num_order(order):
    return (order[0])


def get_cat_id(order):
    return (order[2])


def get_prod_id(order):
    return (order[3])


def get_my_orders(call):
    orders = my_orders_db.get_orders(call)

    text = "Ваши заказы:\n"

    for i in range(0, len(orders)):
        text = text + "№" + str(get_num_order(orders[i])) + ". "
        text = text + "Категория - " + my_orders_db.get_cat_name(get_cat_id(orders[i])) + ". "
        text = text + "Продук - " + my_orders_db.get_prod_name(get_prod_id(orders[i])) + ". \n\n"
    bot.send_message(call.message.chat.id, text = text)
