from telebot.types import InlineKeyboardButton,  ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup

def show_main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn_1 = KeyboardButton("Marvel")
    btn_2 = KeyboardButton("Anime")
    btn_3 = KeyboardButton("Genshin impact")
    markup.add(btn_1, btn_2, btn_3)
    return markup

def return_to_main_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    btn_1 = InlineKeyboardButton("Вернуться в главное меню", callback_data="rtr_tm")
    markup.add(btn_1)
    return markup
