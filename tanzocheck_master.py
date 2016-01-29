#Prova d'uso del modulo tanzocheck.py

from telegram import Updater
import logging
from tanzocheck import Check

check=Check()

# Enable logging
logging.basicConfig(
		format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
		level=logging.INFO)

logger = logging.getLogger(__name__)

def messaggi_in_arrivo(bot, update):
	user_type= check.user(bot,update)
	
	if user_type=="none":
		bot.sendMessage(update.message.chat_id, "Accesso negato")
		return

	if user_type=="user":
		bot.sendMessage(update.message.chat_id, "User: [%s]" % update.message.from_user.username)
		return

	if user_type=="su":
		bot.sendMessage(update.message.chat_id, "Super user: [%s]" % update.message.from_user.username)
		return

def comando_start(bot, update):	
	user_type= check.user(bot,update)
	
	if user_type=="none":
		bot.sendMessage(update.message.chat_id, "Accesso negato")
		return

	if user_type=="user":
		bot.sendMessage(update.message.chat_id, "User: [%s]" % update.message.from_user.username)
		return

	if user_type=="su":
		bot.sendMessage(update.message.chat_id, "Super user: [%s]" % update.message.from_user.username)
		return

def comando_help(bot, update):
	help_text = (
	"/otp Genera una one time password\n"
	"/userlist Lista utenti\n"
	"/userdel Cancella tutti gli utenti\n"
	)
	user_type= check.user(bot,update)
	
	if user_type!="none":
		bot.sendMessage(update.message.chat_id, help_text)
		return

def comando_ciccio(bot, update):
	text = (
	"Bella Ciccio\n"
	)
	user_type= check.user(bot,update)

	if user_type!="none":
		bot.sendMessage(update.message.chat_id, text)
		return

updater = Updater(token='138682670:AAGpVS2brpdVCpJ872ZGl5sbe9KQbFUjAZQ')
dispatcher = updater.dispatcher
dispatcher.addTelegramMessageHandler(messaggi_in_arrivo)
dispatcher.addTelegramCommandHandler("start",comando_start)
dispatcher.addTelegramCommandHandler("help",comando_help)
dispatcher.addTelegramCommandHandler("ciccio",comando_ciccio)
check.addTanzoCheckCommandHandler(dispatcher)
updater.start_polling()
updater.idle()
