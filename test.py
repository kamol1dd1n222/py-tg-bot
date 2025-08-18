from telegram.updater import Updater
from telegram.handlers import MessageHandler
from telegram.types import Update
from config import TOKEN


def handle_message(update: Update):
    message = update.message

    if message.text:
        if message.text == '/start':
            message.reply_text("Assalomu Alaykum! Bizning Echo Botimizga Xush kelibsiz 🙂")
        else:
            message.reply_text(message.text)

    elif 'photo' in message.photo:
        photo = message.photo['photo'][0]['file_id']
        message.reply_photo(photo)

    elif message.sticker:
        message.reply_sticker(message.sticker['file_id'])

    elif message.video:
        message.reply_video(message.video['file_id'])

    elif message.contact:
        message.reply_text(f"Siz raqam yubordingiz: {message.contact['phone_number']}")

    else:
        message.reply_text("Bu turdagi faylni qaytara olmayman 🤷‍♂️")


updater = Updater(TOKEN)
dispatcher = updater.dispatcher

dispatcher.add_handler(MessageHandler(handle_message))

updater.start_polling()
