import os
import telebot

TOKEN = os.getenv("8709005198:AAEIw9YwBKi1iRYn2oQlw_8CR_OWe9XD3ms")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Бот работает ✅")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.send_message(message.chat.id, message.text)

bot.polling()
