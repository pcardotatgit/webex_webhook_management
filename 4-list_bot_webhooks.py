'''
    List all webhooks the Webex Team Bot has
'''
import requests
import json
from crayons import *
import config  as conf

BOT_ACCESS_TOKEN=conf.BOT_ACCESS_TOKEN
version=conf.version

def get_bot_webhooks():
    global BOT_ACCESS_TOKEN
    lines=[]
    if BOT_ACCESS_TOKEN=='':
        with open ('../keys/webex_bot_keys.txt','r') as file:
            content = file.read()
            lines=content.split('\n')
            DESTINATION_ROOM_ID=(lines[0].split(':'))[1]
            BOT_ACCESS_TOKEN=(lines[1].split(':'))[1]
    print(BOT_ACCESS_TOKEN)
    print()
    URL = f'https://webexapis.com/v1/webhooks'
    headers = {'Authorization': 'Bearer ' + BOT_ACCESS_TOKEN,
               'Content-type': 'application/json;charset=utf-8'}
    response = requests.get(URL, headers=headers)
    #print(type(response))
    if response.status_code == 200:
        resultat=json.dumps(response.json(),sort_keys=True,indent=4, separators=(',', ': '))
        print(resultat)
        #result=json.dumps(response.json())
        result=response.json()
        with open('webhooks.txt','w') as file:
            file.write(resultat)
    else:
        # Oops something went wrong...  Better do something about it.
        print(response.status_code, response.text)
    
if __name__ == "__main__":
    print()  
    print(yellow(f'List all webhooks Bot has v{version}',bold=True))
    print() 
    get_bot_webhooks()
    print(yellow("DONE result saved into : webhooks.txt",bold=True))