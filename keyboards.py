from telebot.types import KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup


# keyborad main
def main_keyboard(): 
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.row("BTC")
    return keyboard

