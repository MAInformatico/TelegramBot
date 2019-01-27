# -*- coding:utf-8 -*-
import telebot
from telebot import types
import time

token="" # put the token of our bot
bot = telebot.TeleBot(token) # Inicializar el bot

@bot.message_handler(commands=['website'])
def handle_start(message): bot.reply_to(message, "mainformatico.github.io")

@bot.message_handler(commands=['web'])
def handle_start(message): bot.reply_to(message, "mainformatico.github.io")

@bot.message_handler(commands=['blog'])
def handle_start(message): bot.reply_to(message, "mainformatico.github.io")

@bot.message_handler(commands=['video'])
def handle_video(message): bot.reply_to(message, "https://www.youtube.com/watch?v=EDbCZaAHEXI")

@bot.message_handler(commands=['tiempo'])
def handle_frio(message): bot.reply_to(message, "https://www.eltiempo.es")


@bot.message_handler(func=lambda message: message.text == "hola")
 
def command_text_hola(m): 
    time.sleep(1) 
    bot.send_message(m.chat.id, "¿Qué te cuentas?") 

@bot.message_handler(func=lambda message: message.text == "hi")
 
def command_text_hi(m): 
    time.sleep(1) 
    bot.send_message(m.chat.id, "What's up, dude?") 

@bot.message_handler(func=lambda message: message.text == "salut")
 
def command_text_salut(m): 
    time.sleep(1) 
    bot.send_message(m.chat.id, "Salut! Ça va?") 


@bot.message_handler(func=lambda message: message.text == "examen")
 
def command_text_examen(m): 
    time.sleep(1) 
    bot.send_message(m.chat.id, "Te sobran huevos para aprobarlo, tio. ¡Vamos que se puede!") 


bot.polling()