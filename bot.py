import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, filters
<<<<<<< HEAD
=======
from checker import checker
>>>>>>> 3083944 (updating)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def temperature(update, context):
    verify = checker()
    update.message.reply_text("This is the current temperature of the server:\n" + str(verify.get_temperature()))

def hosts(update, context):
    verify = checker()
    update.message.reply_text("These are the current devices connected into the LAN:\n " + str(verify.get_hosts()))
    
def show_help(update, context):
    update.message.reply_text("You can use these commands: \n" + "/temperature to check server's temperature\n" + "/hosts shows the current hosts connected into your LAN\n")
   
    
def main():
    updater = Updater("your API key here", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("temperature",temperature))
    dp.add_handler(CommandHandler("hosts",hosts))
<<<<<<< HEAD
    dp.add_handler(CommandHandler("hello",hello))
=======
>>>>>>> 3083944 (updating)
    dp.add_handler(CommandHandler("help",show_help))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
