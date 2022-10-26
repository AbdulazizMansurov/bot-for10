from data import bot
import time
from keyboards import *
from telebot.types import Message, ReplyKeyboardRemove, CallbackQuery
from parsers import *



@bot.message_handler()
def give_marvel_n(message: Message):
    chat_id = message.chat.id
    text = " "
    if message.text == "Marvel":
        bot.send_message(chat_id, "Новость подбирается...", reply_markup=ReplyKeyboardRemove())
        while True:
            data = Marvel_News().show_marvel_new()
            if text != data["name"]:
                mess = f"""<b>Новость!<b>\n{data["name"]}
<a href="{data["link"]}">Подробная информация</a>"
Данные взяты с сайта {data["set"]}\n
Спасибо что воспользовались нашим ботом!
<a href="https://t.me/news_for_10_abdu_bot">Бот Абдулазиза</a>
"""
                bot.send_message(chat_id, mess, reply_markup=return_to_main_menu())
                text = data["name"]
                time.sleep(60)

    elif message.text == "Anime":
        bot.send_message(chat_id, "Новость подбирается...", reply_markup=ReplyKeyboardRemove())
        while True:
            data = Anime_parser().show_anime_new()
            if text != data["name"]:
                mess = f"""<b>Новость!</b>\n
{data["name"]}
<a href="{data["link"]}">Подробная информация</a>"
Данные взяты с сайта {data["set"]}\n
Спасибо что воспользовались нашим ботом!
<a href="https://t.me/news_for_10_abdu_bot">Бот Абдулазиза</a>"""
                bot.send_message(chat_id, mess, reply_markup=return_to_main_menu())
                text = data["name"]
                time.sleep(60)

    elif message.text == "Genshin impact":
        bot.send_message(chat_id, "Новость подбирается...", reply_markup=ReplyKeyboardRemove())
        while True:
            data = Genshin_parser().show_genshin_new()
            if text != data["name"]:
                mess = f"""<b>Новость!</b>\n
{data["name"]}
<a href="{data["link"]}">Подробная информация</a>"
Данные взяты с сайта {data["set"]}\n
Спасибо что воспользовались нашим ботом!
<a href="https://t.me/news_for_10_abdu_bot">Бот Абдулазиза</a>"""
                bot.send_message(chat_id, mess, reply_markup=return_to_main_menu())
                text = data["name"]
                time.sleep(60)


@bot.callback_query_handler(func=lambda call: call.data=="rtr_tm")
def ret_to_main_menu(call: CallbackQuery):
    chat_id = call.message.chat.id
    bot.send_message(chat_id, "Выберите катогорию", reply_markup=show_main_menu())
