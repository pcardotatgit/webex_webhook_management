'''
    send a message to a webex team room
'''
import requests
import sys
import config  as conf
from crayons import *

DESTINATION_ROOM_ID=conf.DESTINATION_ROOM_ID
BOT_ACCESS_TOKEN=conf.BOT_ACCESS_TOKEN
version=conf.version

def send_message():
    global BOT_ACCESS_TOKEN
    global DESTINATION_ROOM_ID
    lines=[]
    if BOT_ACCESS_TOKEN=='':
        with open ('../keys/webex_bot_keys.txt','r') as file:
            content = file.read()
            lines=content.split('\n')
            DESTINATION_ROOM_ID=(lines[0].split(':'))[1]
            BOT_ACCESS_TOKEN=(lines[1].split(':'))[1]
    print(DESTINATION_ROOM_ID)
    print(BOT_ACCESS_TOKEN)

    URL = 'https://api.ciscospark.com/v1/messages'

    MESSAGE_TEXT = 'Hello ! ( test from my python script )'

    headers = {'Authorization': 'Bearer ' + BOT_ACCESS_TOKEN,
               'Content-type': 'application/json;charset=utf-8'}
    post_data = {'roomId': DESTINATION_ROOM_ID,
                 'text': MESSAGE_TEXT}
    response = requests.post(URL, json=post_data, headers=headers)
    if response.status_code == 200:
        # Great your message was posted!
        #message_id = response.json['id']
        #message_text = response.json['text']
        print(green("New message succesfully sent",bold=True))
        #print(message_text)
        print("====================")
        print(response)
    else:
        # Oops something went wrong...  Better do something about it.
        print(red(response.status_code, response.text,bold=True))
        
if __name__ == "__main__":
    print()  
    print(yellow(f'Test sending message from bot token to Webex team Room v{version}',bold=True))
    print() 
    send_message()
    
