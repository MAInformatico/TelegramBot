import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from checker import *
from suntime import *

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def hola(update, context):
    update.message.reply_text('Hola, ¿Qué tal estás?')

def hello(update, context):
    update.message.reply_text('Hi, dude')

def weather(update, context):
    update.message.reply_text("Check weather on this link (also available in English too): https://www.eltiempo.es")

def temperature(update, context):
    verify = checker()
    update.message.reply_text("This is the current temperature of the server:\n" + str(verify.getTemperature()))

def hosts(update, context):
    verify = checker()
    update.message.reply_text("These are the current devices connected into the LAN:\n " + str(verify.getHosts()))

def main():
    updater = Updater("put_your_own_token_here", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("hola", hola))
    dp.add_handler(CommandHandler("weather", weather))
    dp.add_handler(CommandHandler("temperature",temperature))
    dp.add_handler(CommandHandler("hosts",hosts))
    dp.add_handler(CommandHandler("hello",hello))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
