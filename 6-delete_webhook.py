'''
   delete a webhook
'''
import requests
import sys
import config  as conf
from crayons import *

DESTINATION_ROOM_ID=conf.DESTINATION_ROOM_ID
BOT_ACCESS_TOKEN=conf.BOT_ACCESS_TOKEN
version=conf.version

def delete_webhook(webhookId):
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
    response = requests.delete(URL, headers=headers)
    if response.status_code == 204:
        # Great your message was posted!
        #message_id = response.json['id']
        #message_text = response.json['text']
        print(green("WebHook succesfuly Deleted",bold=True))
        #print(message_text)
        print("====================")
        print(response)
    else:
        # Oops something went wrong...  Better do something about it.
        print(response.status_code, response.text)#
    
if __name__ == "__main__":
    webhookId = ''
    print()  
    print(yellow(f'Delete an Existing Webhook v{version}',bold=True))
    print() 
    if webhookId=="":
        print()
        print(red("You must update the webhookId variable in this script first",bold=True)) 
        sys.exit()    
    delete_webhook(webhookId)