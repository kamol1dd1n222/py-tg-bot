from telegram.updater import Updater
from config import TOKEN

Updater = Updater(TOKEN)


Updater.start_polling()
