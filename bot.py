import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from checker import *

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def morning(update, context):
    update.message.reply_text("Morning, dude. There are your links: https://hackernoon.com/" + "\n" + "https://hackaday.com/" + "\n" + "https://news.ycombinator.com/" + "\n") 

def hola(update, context):
    update.message.reply_text('Hola, ¿Qué tal estás?')

def weather(update, context):
    update.message.reply_text("https://www.eltiempo.es")

def temperature(update, context):
    verify = checker()
    update.message.reply_text(str(verify.getTemperature()))


def main():
    updater = Updater("1061594945:AAHsQ0YbDOeehQzgyPvyB0-tn_5vZ4S9_K0", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("hola", hola))
    dp.add_handler(CommandHandler("morning", morning))
    dp.add_handler(CommandHandler("weather", weather))
    dp.add_handler(CommandHandler("temperature",temperature))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
