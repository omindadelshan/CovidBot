import os
import telebot

bot = ("Api Her")

@bot.massage_handler(commands=["start"])
def send_welcome(massage):
	bot.reply_to(massage, "Hello Thete Welcome")
	
@bot.massage_handler(commands=["help"])
def send_welcome(massage):
	bot.reply_to(massage, "Hello Thete Help")
	
bot.polling()