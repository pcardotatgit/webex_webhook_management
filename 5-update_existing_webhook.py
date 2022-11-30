'''
    Update the targetURL of a Webex Team Bot
'''
import requests
import sys
import config  as conf
from crayons import *

DESTINATION_ROOM_ID=conf.DESTINATION_ROOM_ID
BOT_ACCESS_TOKEN=conf.BOT_ACCESS_TOKEN
version=conf.version

def update_webhook(targetURL,webhookId):
    global BOT_ACCESS_TOKEN
    lines=[]
    if BOT_ACCESS_TOKEN=='':
        with open ('../keys/webex_bot_keys.txt','r') as file:
            content = file.read()
            lines=content.split('\n')
            BOT_ACCESS_TOKEN=(lines[1].split(':'))[1]
    print(BOT_ACCESS_TOKEN)

    URL = f'https://webexapis.com/v1/webhooks/{webhookId}'
    headers = {'Authorization': 'Bearer ' + BOT_ACCESS_TOKEN,
               'Content-type': 'application/json;charset=utf-8'}
    post_data = {'targetUrl': targetURL}
    response = requests.put(URL, json=post_data, headers=headers)
    if response.status_code == 200:
        # Great your message was posted!
        #message_id = response.json['id']
        #message_text = response.json['text']
        print(green("WebHook succesfuly updated with a new targetURL",bold=True))
        #print(message_text)
        print("====================")
        print(response)
    else:
        # Oops something went wrong...  Better do something about it.
        print(response.status_code, response.text)#
    
if __name__ == "__main__":
    targetURL="" #http://{host}/bot_path/bot_logic.php 
    webhookId = ''
    if targetURL=="":
        print()
        print(red("You must update the targetURL variable in this script first !",bold=True))
        sys.exit()
    if webhookId=="":
        print()
        print(red("You must update the webhookId variable in this script first",bold=True)) 
        sys.exit()
    print()  
    print(yellow(f'Update Existing Webhook v{version}',bold=True))
    print() 
    update_webhook(targetURL,webhookId)