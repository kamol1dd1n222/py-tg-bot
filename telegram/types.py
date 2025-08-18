import requests
from config  import TOKEN


class User:

    def __init__(
            self, 
            id: int, 
            first_name: str, 
            username: str | None
        ):
        self.id = id
        self.first_name = first_name
        self.username = username


class Message:

    def __init__(
            self,
            message_id: int,
            from_user: User,
            text: str | None = None,
            photo: str | None = None,
            sticker: dict | None = None,
            video:dict | None = None,
            contact: str | None = None,
            audio: str|None = None,
            document: str | None = None,
            voice:str | None = None,
            video_note:dict | None = None,
            location:dict | None = None,
            poll:str | None = None
           
        ):
        self.message_id = message_id
        self.from_user = from_user
        self.text = text
        self.photo = photo
        self.video = video
        self.sticker = sticker
        self.contact = contact
        self.audio = audio
        self.document = document
        self.voice = voice
        self.video_note = video_note
        self.location = location
        self.poll = poll
        
        
        
    def reply_text(self, text: str):
        params = {
            'chat_id': self.from_user.id,
            'text': text
        }
        requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage", params=params)
    
    def reply_photo(self,photo:str):
        params = {
            'chat_id':self.from_user.id,
            'photo':photo
        }
        requests.get(f"https://api.telegram.org/bot{TOKEN}/sendPhoto",params=params)
    
    def reply_sticker(self,file_id:str):
        params = {
            'chat_id':self.from_user.id,
            'sticker':file_id
        }
        requests.get(f"https://api.telegram.org/bot{TOKEN}/sendSticker",params=params)
    
    def reply_video(self,file_id:str):
        params = {
            'chat_id':self.from_user.id,
            'video':file_id
        }
    
        requests.get(f"https://api.telegram.org/bot{TOKEN}/sendVideo",params=params)
   
    def reply_contact( self,phone_number: str, first_name: str, last_name: str = None):
        
        params = {
        'chat_id':self.from_user.id,
        'phone_number': phone_number,
        'first_name': first_name,
        'last_name': last_name
        }
        requests.get(f"https://api.telegram.org/bot{TOKEN}/sendContact", params=params)
    def reply_audio(self,file_id:str):
        params = {
            'chat_id':self.from_user.id,
            'audio':file_id
        }
    
        requests.get(f"https://api.telegram.org/bot{TOKEN}/sendAudio",params=params)
    
    def reply_document(self,file_id:str):
        params = {
            'chat_id':self.from_user.id,
            'document':file_id
        }
        requests.get(f"https://api.telegram.org/bot{TOKEN}/sendDocument",params=params)

    def reply_voice(self,file_id:str):
        params = {
            'chat_id':self.from_user.id,
            'voice':file_id
        }
    
        requests.get(f"https://api.telegram.org/bot{TOKEN}/sendVoice",params=params)

    def reply_video_note(self,file_id:str):
        params = {
            'chat_id':self.from_user.id,
            'video_note':file_id
        }
    
        requests.get(f"https://api.telegram.org/bot{TOKEN}/sendVideoNote",params=params)
    def reply_location(self,latitude:float,longitude:float):
        params = {
            'chat_id':self.from_user.id,
            'latitude':latitude,
            'longitude':longitude
        }
        requests.get(f"https://api.telegram.org/bot{TOKEN}/sendLocation",params=params)

    def reply_poll(self, question, options):
        
        params = {
            "chat_id": self.from_user.id,
            "question": question,
            "options": str(options).replace("'", '"')  
        }
        requests.get( f"https://api.telegram.org/bot{TOKEN}/sendPoll",params=params)


class Update:

    def __init__(
            self,
            update_id: int, 
            message: Message | None = None,
            edited_message: Message | None = None,
        ) -> None:
        self.update_id = update_id
        self.message = message
        self.edited_message = edited_message