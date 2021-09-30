import os
import telebot

bot = ("1843767480:AAG6y4JwKS5ndgpsCWmsM1JeLBcKmCyXyQc")

@bot.massage_handler(commands=["start"])
def send_welcome(massage):
	bot.reply_to(massage, "Hello Thete Welcome")
	
@bot.massage_handler(commands=["help"])
def send_welcome(massage):
	bot.reply_to(massage, "Hello Thete Help")
	
bot.polling()
