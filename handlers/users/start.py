from data import bot
from telebot.types import Message
from config import permitted_users
from keyboards import show_main_menu

@bot.message_handler(commands=["start"])
def start(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Добро пожаловать в бота.\nВыберите категорию", reply_markup=show_main_menu())