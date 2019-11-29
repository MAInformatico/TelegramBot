# -*- coding:utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler
import requests
import re

def morning(bot,update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="Morning, dude. There are your links: https://hackernoon.com/" + "\n" + "https://hackaday.com/" + "\n" + "https://www.genbeta.com/" + "\n") 

def hola(bot,update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="Hola, ¿Qué tal estás?") 

def weather(bot,update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="https://www.eltiempo.es")



def main():

    updater = Updater('<insert your bot token>')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('morning',morning))    
    dp.add_handler(CommandHandler('hola',hola))
    dp.add_handler(CommandHandler('weather',weather))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()