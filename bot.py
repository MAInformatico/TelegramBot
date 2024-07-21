import logging

from checker import checker
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logging.getLogger("httpx").setLevel(logging.WARNING)


logger = logging.getLogger(__name__)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.warning('Update "%s" caused error "%s"', update, context.error)

async def temperature(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    verify = checker()
    await update.message.reply_text("This is the current temperature of the server:\n" + str(verify.get_temperature()))

async def hosts(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    verify = checker()
    await update.message.reply_text("These are the current devices connected into the LAN:\n " + str(verify.get_hosts()))
    
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("You can use these commands: \n" + "/temperature to check server's temperature\n" + "/hosts shows the current hosts connected into your LAN\n")
   
    
def main() -> None:
    application  = Application.builder().token("your_token_here").build()

    application.add_handler(CommandHandler("temperature",temperature))
    application.add_handler(CommandHandler("hosts",hosts))
    application.add_handler(CommandHandler("help",help))


    #application.run_polling()
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()
