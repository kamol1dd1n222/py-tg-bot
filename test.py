from telegram.updater import Updater
from telegram.handlers import MessageHandler
from telegram.types import Update
from config import TOKEN


def handle_message(update: Update):
    message = update.message

    if message.text:
        if message.text == '/start':
            message.reply_text("Assalomu Alaykum! Bizning Echo Botimizga Xush kelibsiz!")
        else:
            message.reply_text(message.text)

    elif message.photo:
        photo = message.photo[0]['file_id']
        message.reply_photo(photo)

    elif message.sticker:
        message.reply_sticker(message.sticker['file_id'])

    elif message.video:
        message.reply_video(message.video['file_id'])

    elif message.contact:
        message.reply_contact(message.contact['phone_number'],
                              message.contact['first_name'],
                              message.contact.get('last_name')
                              )
    elif message.audio:
        message.reply_audio(message.audio['file_id'])
    elif message.document:
        message.reply_document(message.document['file_id'])
    elif message.voice:
        message.reply_voice(message.voice['file_id'])
    elif message.video_note:
        message.reply_video_note(message.video_note['file_id'])
    elif message.location:
        message.reply_location(message.location['latitude'],message.location['longitude'])
    elif message.poll:
        question = message.poll["question"]
        options = [opt["text"] for opt in message.poll["options"]]
        message.reply_poll(question, options)


    else:
        message.reply_text("Bu turdagi faylni qaytara olmayman ")


updater = Updater(TOKEN)
dispatcher = updater.dispatcher

dispatcher.add_handler(MessageHandler(handle_message))

updater.start_polling()
