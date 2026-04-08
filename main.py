import os
import telebot

TOKEN = os.getenv("8709005198:AAG0SB65EJZR6leqzNpCL3RYpi8_7_ipeKo")

print("TOKEN:", TOKEN)

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Бот работает ✅")

bot.polling()
