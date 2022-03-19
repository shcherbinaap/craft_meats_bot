from craft_meats_bot.my_data import bot

def contact_us(call):
    TEXT = "Написать создателю @Andrei_shcherbina"
    bot.send_message(call.message.chat.id, text = TEXT)

