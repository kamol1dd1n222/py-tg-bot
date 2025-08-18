import time
import requests
from .dispatcher import Dispatcher
from .types import Update, Message, User


class Updater:

    def __init__(self, token: str):
        self.token = token
        self.offset = None
        self.dispatcher = Dispatcher()

    def get_updates(self):
        params = {"offset": self.offset}
        response = requests.get(f"https://api.telegram.org/bot{self.token}/getUpdates", params=params)
        data = response.json()


        if not data.get("ok"):
            data = []     
            print("Xato")        
        else:
            data = data["result"]  

        updates: list[Update] = []
        for item in data:
            update = Update(update_id=item['update_id'])

            if 'message' in item:
                user = User(
                    id=item['message']['from']['id'], 
                    first_name=item['message']['from']['first_name'],
                    username=item['message']['from']['username']
                )
                message = Message(
                    message_id=item['message']['message_id'], 
                    from_user=user
                )

                if 'text' in item['message']:
                    message.text = item['message']['text']
                if 'photo' in item['message']:
                    message.photo = item['message']['photo']
                if 'sticker' in item['message']:
                    message.sticker = item['message']['sticker']
                if 'video' in item['message']:
                    message.video = item['message']['video']
                if 'contact' in item['message']:
                    message.contact = item['message']['contact']
                if 'audio' in item['message']:
                    message.audio = item['message']['audio']
                if 'document' in item['message']:
                    message.document = item['message']['document']
                if 'voice' in item['message']:
                    message.voice = item['message']['voice']
                if "video_note" in item['message']:
                    message.video_note = item['message']['video_note']
                if 'location' in item['message']:
                    message.location = item['message']['location']
                if 'poll' in item['message']:
                    message.poll = item['message']['poll']
                update.message = message
            updates.append(update)

        return updates

    def start_polling(self):

        while True:
            
            updates = self.get_updates()
            for update in updates:

                self.dispatcher.process_update(update)

                self.offset = update.update_id + 1

            time.sleep(1)