import json
import requests
import os
from dotenv import load_dotenv

 
load_dotenv()
API_KEY = os.getenv('API_KEY')
API_TOKEN = os.getenv('API_TOKEN')
BOARD_ID = os.getenv('BOARD_ID')
print(API_KEY)
print(API_TOKEN)


def api(endpoint):
    boardId = BOARD_ID
    url = "https://api.trello.com/1/boards/" + boardId + "/"

    query = {
    'key': API_KEY,
    'token': API_TOKEN
    }

    response = requests.request(
    "GET",
    url + endpoint,
    params=query
    )

    data = json.loads(response.text)
    return data

list_map = {}
for l in api("lists"):
    list_map[l["id"]] = l["name"]


#print(list_map)

list_to_card = {}
for c in api("cards"):
    if c["idList"] in list_to_card:
        list_to_card[c["idList"]].append(c)
    else:
        list_to_card[c["idList"]] = [c]

for l in list_to_card:
    print(list_map[l])
    print(len(list_to_card[l]))
    '''
    for c in list_to_card[l]:
        print("\n" + c["name"])
        '''


