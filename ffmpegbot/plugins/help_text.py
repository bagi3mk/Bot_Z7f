from pyrogram import Client, filters
import re,time
from ffmpegbot import (Channel_Stor,Time_Sleep)


@Client.on_message(filters.me & filters.text)
def Start_One(client,message):
    chat = message.chat.id
    msg = message.text
    msi = message.message_id
    if re.match("انيك امك يا (.*?)$", msg):
        name_of_anime = re.match("انيك امك يا (.*?) ب (.*?)$", msg).group(1)
        much = 0
        for messagel in client.iter_history(Channel_Stor):
            if messagel.text != None:
                if much == 20:
                    break
                time.sleep(Time_Sleep)
                client.send_message(chat, str(messagel.text).replace("ـ", name_of_anime))
                much += 1
