from telebot import types

ORDER = "order"

INFO_ABOUT_US = "info_about_us"
DOSTAVKA = 'dostavka'
COMMENT = 'comment'
CONTACT = 'contact'
GET_ORDER_INFO = 'get_order_info'
GET_STORAGE_INFO = "get_storage_info"
PUT_STORAGE_INFO = "put_storage_info"
BUYING_MEATS = "buying_meat"
MEATS_INFO = "meats_info"
MY_ORDERS = "my_orders"

APP = "app="
CATEGORY = "cat_id="
PRODUCT = "prod_id="
QUANTITY = "quantity="
STORAGE = "stor_id="
BUTTON = "btn="

button_start_order = types.InlineKeyboardButton(text = 'Сделать заказ', callback_data = APP + ORDER)
button_info_about_us = types.InlineKeyboardButton(text = 'Информация о нас', callback_data = INFO_ABOUT_US)
button_dostavka_info = types.InlineKeyboardButton(text = 'Узнать о доставке', callback_data = DOSTAVKA)
button_comment_send = types.InlineKeyboardButton(text = 'Оставить отзыв', callback_data = COMMENT)
button_get_contact = types.InlineKeyboardButton(text = 'Контакты', callback_data = CONTACT)
button_order_info = types.InlineKeyboardButton(text = 'Информация о заказе', callback_data = GET_ORDER_INFO)
button_get_storage_info = types.InlineKeyboardButton(text = 'Наличие продукции', callback_data = APP + GET_STORAGE_INFO)
button_put_storage_info = types.InlineKeyboardButton(text = 'Добавить продукцию', callback_data = PUT_STORAGE_INFO)
button_buying_meat = types.InlineKeyboardButton(text = 'Покупка сырья', callback_data = BUYING_MEATS)
button_meats_info = types.InlineKeyboardButton(text = 'Информация о мясе', callback_data = MEATS_INFO)
button_my_orders = types.InlineKeyboardButton(text = 'Мои заказы', callback_data = MY_ORDERS)