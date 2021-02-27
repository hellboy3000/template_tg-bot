import telebot as tl
from util import *
from keyboards import *


bot = tl.TeleBot('<YOUR TOKEN>') # api token


@bot.message_handler(func=lambda message: message.text=='BTC') # output of the function of the bitcoin rate 
def bitcoin_handler(message): 
    msg = bitcoin_to_usd()    
    bot.send_message(message.chat.id, msg)
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAALjGmA4AeYWu3d81ki-qJs7x08w9NK0AAL8BQAClvoSBfP45oIb_tb9HgQ')    
 

@bot.message_handler(commands=['start'])
def hello_message(message):   
    bot.send_message(message.chat.id, 'Привет ＼(≧▽≦)／', reply_markup=main_keyboard()) # start command displays keyboard and message


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.chat.id, 'Я не знаю что ответить 😢, пропишите /start') # this is displayed when an unknown message arrives


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
